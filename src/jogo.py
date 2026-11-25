import pygame


from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    RAIO_LUPA,
    LADO_PARTICIPANTE,
    TAMANHO_FONTE_TITULO,
    TAMANHO_FONTE_NOME,
    CINZA,
    PRETO,
    BRANCO,
    AZUL_NOTURNO,
    PAINEL_X,
    PAINEL_LARGURA,
    COR_PAINEL,
    TAMANHO_FONTE_PISTA,
    ESPACO_LINHA,
    INDENTACAO_PISTA,
    MARGEM_ESQUERDA,
    CAMINHO_SPRITES,
)
from src.participante import Participante
from src.lupa import Lupa
from src.rodada import preparar_rodada

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
        Participante("Ana", 150, 200, (90, 160, 250)),
        Participante("Laerte", 450, 200, (255, 150, 90)),
        Participante("Paulo", 150, 400, (120, 200, 130)),
        Participante("Saul", 450, 400, (230,  110, 170)),            
    ] 
    estado = "menu"
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
                    estado = "jogando"
                elif event.key == pygame.K_ESCAPE:
                    # ESC volta ao menu; no menu, ele fecha o jogo
                    if estado == "jogando":
                        estado = "menu"
                    elif estado == "menu":
                        rodando = False

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
                if participante.esta_sob(local_mouse):
                    # inflate(12, 12) devolve uma cópia do quadrado 12 pixels
                    # maior (6 de cada lado); o 3 é a espessura da linha
                    pygame.draw.rect(tela, BRANCO, participante.rect.inflate(12, 12), 3)    
                    sob_lupa = participante

             # atualizar devolve True no frame em que o escaneamento completa;
            # aí a pista do participante escaneado é revelada
            if lupa.atualizar(sob_lupa, tempo_decorrido):
                lupa.escaneando.revelar_pista()

            # painel de Pistas 
            # fundo do painel; é desenhado antes dos textos para ficar por baixo
            pygame.draw.rect(tela, COR_PAINEL, (PAINEL_X, 0, PAINEL_LARGURA, ALTURA_TELA))
            # linha_y é a posição vertical da linha que vai ser escrita; desce a
            # cada linha escrita, como a caneta descendo no caderno
            linha_y = 20
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

            #Lupa
             # desenhada por último para ficar por cima de tudo
            pygame.draw.circle(tela, CINZA, (local_mouse), RAIO_LUPA)

        # mostra na janela o que foi desenhado neste frame
        pygame.display.flip()

    pygame.quit()