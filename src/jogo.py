import pygame


from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    RAIO_LUPA,
    LADO_PARTICIPANTE,
    BARRA_MAXIMO,
    AUMENTO_ESCANEAMENTO,
    BARRA_X,
    BARRA_Y,
    BARRA_LARGURA,
    BARRA_ALTURA,
    COR_BARRA,
    COR_FUNDO_BARRA,
    TAMANHO_FONTE_TITULO,
    TAMANHO_FONTE_NOME,
    CINZA,
    PRETO,
    BRANCO,
    AZUL_NOTURNO,
    PAINEL_X,
    PAINEL_LARGURA,
    COR_PAINEL,
    COR_SUSPEITO,
    TAMANHO_FONTE_PISTA,
    ESPACO_LINHA,
    INDENTACAO_PISTA,
    MARGEM_ESQUERDA,
    CAMINHO_SPRITES,
)
from src.participante import Participante
from src.lupa import Lupa
from src.rodada import preparar_rodada
from src.barra import BarraInfluencia

def executar_jogo():
    """
    Abre a janela e roda o jogo até o jogador fechar.

    Informações relevantes:
        Tem dois estados: "menu" (tela inicial) e "jogando"
        Em cada volta do while (um frame) o jogo faz sempre 3 coisas:
        1) lê os eventos (teclado, fechar a janela)
        2) atualiza o que mudou (lupa, pistas)
        3) desenha tudo do zero e mostra na tela
    """
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    # as fontes são criadas UMA vez aqui, fora do loop, e só depois do pygame.init()
    fonte_titulo = pygame.font.Font(None, TAMANHO_FONTE_TITULO)
    fonte_nome = pygame.font.Font(None, TAMANHO_FONTE_NOME)
    fonte_pista = pygame.font.Font(None, TAMANHO_FONTE_PISTA)

    relogio = pygame.time.Clock()
    rodando = True

    # os 4 participantes: (nome, x do centro, y do centro, cor RGB)
    participantes = [
        Participante("Ana", 100, 230, (90, 160, 250)),
        Participante("Laerte", 600, 230, (255, 150, 90)),
        Participante("Paulo", 100, 460, (120, 200, 130)),
        Participante("Saul", 600, 460, (230,  110, 170)),            
    ] 
    estado = "menu"
    suspeito = None
    barra = BarraInfluencia()
    lupa = Lupa()

    while rodando:

        # O dt faz o tempo ser o mesmo em qualquer computador
        tempo_decorrido = relogio.tick(FPS) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and estado == "menu":
                    # começa a rodada: sorteia a IA e distribui as pistas
                    preparar_rodada(participantes)
                    suspeito = None
                    barra = BarraInfluencia()
                    estado = "jogando"
                elif event.key == pygame.K_RETURN and estado in ("vitoria", "derrota"):
                    estado = "menu"
                elif event.key == pygame.K_SPACE and estado == "jogando" and suspeito is not None:
                    if suspeito.eh_ia:
                        estado = "vitoria"
                    else:
                        estado = "derrota"
                elif event.key == pygame.K_ESCAPE:
                    # ESC volta ao menu; no menu, ele fecha o jogo
                    if estado == "jogando":
                        estado = "menu"
                    elif estado == "menu":
                        rodando = False
            # Marcação de suspeito 
            elif event.type == pygame.MOUSEBUTTONDOWN and estado == "jogando":
                if event.button == 1:
                    for participante in participantes:
                        if participante.esta_sob(event.pos):
                            if participante is suspeito:
                                suspeito = None
                            else:
                                suspeito = participante

        # posição atual do mouse: (x, y) 
        # lembrem de usar a variavel e n get_pos() toda hora
        local_mouse = pygame.mouse.get_pos()  
        tela.fill(AZUL_NOTURNO)

        if estado == "menu":
            surface = fonte_titulo.render(TITULO_JOGO, True, BRANCO)
            retangulo = surface.get_rect(center=(LARGURA_TELA // 2, 200))
            tela.blit(surface, retangulo)
            orientacao = fonte_titulo.render("Pressione ENTER para jogar", True, BRANCO)
            retangulo = orientacao.get_rect(center=(LARGURA_TELA // 2, 300))
            tela.blit(orientacao, retangulo)
            # uma Lupa nova a cada frame no menu: zera o escaneamento ao voltar
            lupa = Lupa()
        elif estado == "jogando":
            # sob_lupa guarda quem está com o mouse em cima neste frame
            sob_lupa = None
            for participante in participantes:
                participante.desenhar(tela, fonte_nome)
                if participante is suspeito:
                    pygame.draw.rect(tela, COR_SUSPEITO, participante.rect.inflate(5, 5), 3)
                    surface = fonte_nome.render("SUSPEITO", True, COR_SUSPEITO)
                    retangulo = surface.get_rect(center=(participante.rect.centerx, participante.rect.bottom + 20))
                    tela.blit(surface, retangulo)
                if participante.esta_sob(local_mouse):
                    # inflate(12, 12) devolve uma cópia do quadrado 12 pixels
                    # maior (6 de cada lado); o 3 é a espessura da linha
                    pygame.draw.rect(tela, BRANCO, participante.rect.inflate(10, 10), 3)    
                    sob_lupa = participante

            # atualizar devolve True no frame em que o escaneamento completa
            # aí a pista do participante escaneado é revelada
            if lupa.atualizar(sob_lupa, tempo_decorrido):
                if lupa.escaneando.revelar_pista():
                   barra.subir_escaneamento(AUMENTO_ESCANEAMENTO)

            barra.atualizar(tempo_decorrido)
            if barra.encheu():
                estado = "derrota"

            # painel de Pistas 
            pygame.draw.rect(tela, COR_PAINEL, (PAINEL_X, 100, PAINEL_LARGURA, ALTURA_TELA))
            # linha_y é a posição vertical da linha que vai ser escrita; desce a
            # cada linha escrita, como a caneta descendo no caderno
            linha_y = 120
            for participante in participantes:
                surface = fonte_nome.render(participante.nome, True, BRANCO)
                tela.blit(surface, (PAINEL_X + MARGEM_ESQUERDA, linha_y))
                linha_y += ESPACO_LINHA
                for pista in participante.pistas_reveladas:
                    surface = fonte_pista.render("- " + pista, True, CINZA)
                    tela.blit(surface, (PAINEL_X + INDENTACAO_PISTA, linha_y))
                    linha_y += ESPACO_LINHA
                # linha em branco entre um participante e o próximo
                linha_y += ESPACO_LINHA

            # barra de influência
            pygame.draw.rect(tela, COR_FUNDO_BARRA, (BARRA_X, BARRA_Y, BARRA_LARGURA, BARRA_ALTURA))
            largura_cheia = int(BARRA_LARGURA * barra.valor_atual / BARRA_MAXIMO)
            pygame.draw.rect(tela, COR_BARRA, (BARRA_X, BARRA_Y, largura_cheia, BARRA_ALTURA))
            texto = fonte_nome.render("Influência da IA: " + str(int(barra.valor_atual)) + "%", True, BRANCO)
            tela.blit(texto, (BARRA_X, BARRA_Y - 28))

            #Lupa
             # desenhada por último para ficar por cima de tudo
            pygame.draw.circle(tela, CINZA, (local_mouse), RAIO_LUPA)

        elif estado == "vitoria" or estado == "derrota":
            if estado == "vitoria":
                mensagem = "Parabéns você encontrou a IA!"
            else:
                mensagem = "Você deixou a IA dominar"
            surface = fonte_titulo.render(mensagem, True, BRANCO)
            retangulo = surface.get_rect(center=(LARGURA_TELA // 2, 250))
            tela.blit(surface, retangulo)
            orientacao = fonte_nome.render("Pressione ENTER para voltar ao menu", True, CINZA)
            retangulo = orientacao.get_rect(center=(LARGURA_TELA // 2, 320))
            tela.blit(orientacao, retangulo)
        # mostra na janela o que foi desenhado neste frame
        pygame.display.flip()

    pygame.quit()