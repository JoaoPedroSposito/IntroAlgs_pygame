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
from src.participante import Participante

def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    fonte_48 = pygame.font.Font(None,48)
    fonte_24 = pygame.font.Font(None,24)

    relogio = pygame.time.Clock()
    rodando = True

    participantes = [
        Participante("Ana", 150, 200, (90, 160, 250)),
        Participante("Laerte", 450, 200, (255, 150, 90)),
        Participante("Paulo", 150, 400, (120, 200, 130)),
        Participante("Saul", 450, 400, (230,  110, 170)),            
    ] 
    estado = "menu"
    investigando = None
    progresso = 0

    while rodando:
        tempo_decorrido = relogio.tick(FPS) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and estado == "menu":
                    estado = "jogando"
                elif event.key == pygame.K_ESCAPE:
                    if estado == "jogando":
                        estado = "menu"
                    elif estado == "menu":
                        rodando = False


        mouse = pygame.mouse.get_pos()  
        tela.fill(AZUL_NOTURNO)

        if estado == "menu":
            surface = fonte_48.render(TITULO_JOGO, True, BRANCO)
            retangulo = surface.get_rect(center=(LARGURA_TELA // 2, 200))
            tela.blit(surface, (280, 200))
            orientacao = fonte_48.render("Pressione ENTER para jogar", True, BRANCO)
            retangulo = orientacao.get_rect(center=(LARGURA_TELA // 2, 300))
            tela.blit(orientacao, retangulo)
            investigando = None
            progresso = 0
        elif estado == "jogando":
            sob_lupa = None
            for p in participantes:
                p.desenhar(tela, fonte_24)
                if p.esta_sob(mouse):
                    pygame.draw.circle(tela, BRANCO, (p.x, p.y), p.raio + 6, 3)
                    sob_lupa = p
            if sob_lupa is not None and sob_lupa is investigando:
                progresso += tempo_decorrido
            else:
                investigando = sob_lupa
                progresso = 0

            if progresso >= 1.5:
                print("Pista revelada")
                progresso = 0         
            pygame.draw.circle(tela, CINZA, (mouse), 20)

        
        pygame.display.flip()

    pygame.quit()