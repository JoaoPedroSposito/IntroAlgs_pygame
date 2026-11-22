import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    RAIO_LUPA,
    TAMANHO_FONTE_TITULO,
    TAMANHO_FONTE_NOME,
    CINZA,
    PRETO,
    BRANCO,
    AZUL_NOTURNO,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)
from src.participante import Participante
from src.lupa import Lupa

def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    fonte_titulo = pygame.font.Font(None, TAMANHO_FONTE_TITULO)
    fonte_nome = pygame.font.Font(None, TAMANHO_FONTE_NOME)

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
                    estado = "jogando"
                elif event.key == pygame.K_ESCAPE:
                    if estado == "jogando":
                        estado = "menu"
                    elif estado == "menu":
                        rodando = False


        mouse = pygame.mouse.get_pos()  
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
            for p in participantes:
                p.desenhar(tela, fonte_nome)
                if p.esta_sob(mouse):
                    pygame.draw.circle(tela, BRANCO, (p.x, p.y), p.raio + 6, 3)
                    sob_lupa = p

            if lupa.atualizar(sob_lupa, tempo_decorrido):
                print("Pista revelada")
            #Lupa
            pygame.draw.circle(tela, CINZA, (mouse), RAIO_LUPA)

        
        pygame.display.flip()

    pygame.quit()