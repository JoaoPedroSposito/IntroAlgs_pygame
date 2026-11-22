import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    PRETO,
    BRANCO,
    AZUL_NOTURNO,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)

def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    while rodando:

        tempo_decorrido = relogio.tick(FPS) / 1000
        tela.fill(AZUL_NOTURNO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                rodando = False

        pygame.display.flip()

    pygame.quit()