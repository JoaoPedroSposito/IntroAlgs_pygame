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
    while rodando:
        tempo_decorrido = relogio.tick(FPS) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                if estado == "menu" and event.key == pygame.K_RETURN:
                    estado = "jogando"                
                elif event.key == pygame.K_ESCAPE:
                    rodando = False

        mouse = pygame.mouse.get_pos()  
        tela.fill(AZUL_NOTURNO)

        if estado == "menu":
            surface = fonte_48.render(TITULO_JOGO, True, BRANCO)
            tela.blit(surface, (280, 200))
            orientacao = fonte_48.render("Pressione ENTER para jogar", True, BRANCO)
            tela.blit(orientacao, (180, 300))
        elif estado == "jogando":
            pygame.draw.circle(tela, CINZA, (pygame.mouse.get_pos()), 20)
            for p in participantes:
                        p.desenhar(tela, fonte_24)
                        if p.esta_sob(mouse):
                            pygame.draw.circle(tela, BRANCO, (p.x, p.y), p.raio + 6, 3)
                            "print(p.nome)"
        

        
        pygame.display.flip()

    pygame.quit()