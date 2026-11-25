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
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)
from src.participante import Participante
from src.lupa import Lupa
from src.rodada import preparar_rodada

def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    fonte_titulo = pygame.font.Font(None, TAMANHO_FONTE_TITULO)
    fonte_nome = pygame.font.Font(None, TAMANHO_FONTE_NOME)
    fonte_pista = pygame.font.Font(None, TAMANHO_FONTE_PISTA)

    relogio = pygame.time.Clock()
    rodando = True

    participantes = [
        Participante("Ana", 150, 200, (90, 160, 250)),
        Participante("Laerte", 450, 200, (255, 150, 90)),
        Participante("Paulo", 150, 400, (120, 200, 130)),
        Participante("Saul", 450, 400, (230,  110, 170)),            
    ] 
    estado = "menu"
    lupa = Lupa()

    while rodando:
        tempo_decorrido = relogio.tick(FPS) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and estado == "menu":
                    preparar_rodada(participantes)
                    estado = "jogando"
                elif event.key == pygame.K_ESCAPE:
                    if estado == "jogando":
                        estado = "menu"
                    elif estado == "menu":
                        rodando = False


        local_mouse = pygame.mouse.get_pos()  
        tela.fill(AZUL_NOTURNO)

        if estado == "menu":
            surface = fonte_titulo.render(TITULO_JOGO, True, BRANCO)
            retangulo = surface.get_rect(center=(LARGURA_TELA // 2, 200))
            tela.blit(surface, retangulo)
            orientacao = fonte_titulo.render("Pressione ENTER para jogar", True, BRANCO)
            retangulo = orientacao.get_rect(center=(LARGURA_TELA // 2, 300))
            tela.blit(orientacao, retangulo)
            lupa = Lupa()
        elif estado == "jogando":
            sob_lupa = None
            for participante in participantes:
                participante.desenhar(tela, fonte_nome)
                if participante.esta_sob(local_mouse):
                    pygame.draw.rect(tela, BRANCO, participante.rect.inflate(12, 12), 3)    
                    sob_lupa = participante

            if lupa.atualizar(sob_lupa, tempo_decorrido):
                lupa.escaneando.revelar_pista()

            # painel de Pistas 
            pygame.draw.rect(tela, COR_PAINEL, (PAINEL_X, 0, PAINEL_LARGURA, ALTURA_TELA))
            linha_y = 20
            for participante in participantes:
                surface = fonte_nome.render(participante.nome, True, BRANCO)
                tela.blit(surface, (PAINEL_X + MARGEM_ESQUERDA, linha_y))
                linha_y += ESPACO_LINHA
                for pista in participante.pistas_reveladas:
                    surface = fonte_pista.render("- " + pista, True, CINZA)
                    tela.blit(surface, (PAINEL_X + INDENTACAO_PISTA, linha_y))
                    linha_y += ESPACO_LINHA
                linha_y += ESPACO_LINHA

            #Lupa
            pygame.draw.circle(tela, CINZA, (local_mouse), RAIO_LUPA)

        
        pygame.display.flip()

    pygame.quit()