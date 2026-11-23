import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    RAIO_LUPA,
    VIDAS_INICIAIS,
    TAMANHO_FONTE_TITULO,
    TAMANHO_FONTE_NOME,
    TAMANHO_FONTE_PISTA,
    LARGURA_PAINEL,
    LIMITE_LINHA_PAINEL,
    CINZA,
    PRETO,
    BRANCO,
    AZUL_NOTURNO,
    AZUL_PAINEL,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)
from src.funcoes import quebrar_texto, jogador_perdeu
from src.participante import Participante
from src.lupa import Lupa
from src.rodada import preparar_rodada, acusar


def criar_participantes():
    return [
        Participante("Ana", 150, 200, (90, 160, 250)),
        Participante("Laerte", 450, 200, (255, 150, 90)),
        Participante("Paulo", 150, 400, (120, 200, 130)),
        Participante("Saul", 450, 400, (230,  110, 170)),
    ]


def iniciar_partida(jogo, participantes):
    preparar_rodada(participantes)
    jogo["vidas"] = VIDAS_INICIAIS
    jogo["lupa"] = Lupa()
    jogo["estado"] = "jogando"


def acusar_com_clique(jogo, participantes, posicao):
    for p in participantes:
        if p.esta_sob(posicao) and not p.mudo:
            acertou, vidas = acusar(p, jogo["vidas"])
            jogo["vidas"] = vidas
            if acertou:
                jogo["estado"] = "vitoria"
            elif jogador_perdeu(vidas):
                jogo["estado"] = "derrota"


def tratar_eventos(jogo, participantes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo["rodando"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if jogo["estado"] == "menu":
                    iniciar_partida(jogo, participantes)
                elif jogo["estado"] in ("vitoria", "derrota"):
                    jogo["estado"] = "menu"
            elif event.key == pygame.K_ESCAPE:
                if jogo["estado"] == "menu":
                    jogo["rodando"] = False
                else:
                    jogo["estado"] = "menu"
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if jogo["estado"] == "jogando":
                acusar_com_clique(jogo, participantes, event.pos)


def atualizar_partida(jogo, participantes, mouse, tempo_decorrido):
    sob_lupa = None
    for p in participantes:
        if p.esta_sob(mouse):
            sob_lupa = p

    lupa = jogo["lupa"]
    if lupa.atualizar(sob_lupa, tempo_decorrido):
        lupa.escaneando.revelar_pista()


def desenhar_menu(tela, fonte_titulo):
    surface = fonte_titulo.render(TITULO_JOGO, True, BRANCO)
    retangulo = surface.get_rect(center=(LARGURA_TELA // 2, 200))
    tela.blit(surface, retangulo)
    orientacao = fonte_titulo.render("Pressione ENTER para jogar", True, BRANCO)
    retangulo = orientacao.get_rect(center=(LARGURA_TELA // 2, 300))
    tela.blit(orientacao, retangulo)


def desenhar_fim(tela, fonte_titulo, mensagem):
    surface = fonte_titulo.render(mensagem, True, BRANCO)
    retangulo = surface.get_rect(center=(LARGURA_TELA // 2, 200))
    tela.blit(surface, retangulo)
    orientacao = fonte_titulo.render("ENTER para voltar ao menu", True, BRANCO)
    retangulo = orientacao.get_rect(center=(LARGURA_TELA // 2, 300))
    tela.blit(orientacao, retangulo)


def desenhar_painel(tela, fonte_nome, fonte_pista, participantes):
    x = LARGURA_TELA - LARGURA_PAINEL
    pygame.draw.rect(tela, AZUL_PAINEL, (x, 0, LARGURA_PAINEL, ALTURA_TELA))
    y = 20
    for p in participantes:
        if len(p.pistas_reveladas) > 0:
            tela.blit(fonte_nome.render(p.nome, True, p.cor), (x + 15, y))
            y += 26
            for pista in p.pistas_reveladas:
                for linha in quebrar_texto(pista, LIMITE_LINHA_PAINEL):
                    tela.blit(fonte_pista.render(linha, True, BRANCO), (x + 15, y))
                    y += 20
                y += 4
            y += 12


def desenhar_partida(tela, fonte_nome, fonte_pista, jogo, participantes, mouse):
    for p in participantes:
        p.desenhar(tela, fonte_nome)
        if p.esta_sob(mouse):
            pygame.draw.circle(tela, BRANCO, (p.x, p.y), p.raio + 6, 3)

    desenhar_painel(tela, fonte_nome, fonte_pista, participantes)
    vidas = fonte_nome.render("Vidas: " + str(jogo["vidas"]), True, BRANCO)
    tela.blit(vidas, (15, 15))
    #Lupa
    pygame.draw.circle(tela, CINZA, (mouse), RAIO_LUPA)


def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    fonte_titulo = pygame.font.Font(None, TAMANHO_FONTE_TITULO)
    fonte_nome = pygame.font.Font(None, TAMANHO_FONTE_NOME)
    fonte_pista = pygame.font.Font(None, TAMANHO_FONTE_PISTA)

    relogio = pygame.time.Clock()
    participantes = criar_participantes()
    jogo = {"estado": "menu", "vidas": VIDAS_INICIAIS, "lupa": Lupa(), "rodando": True}

    while jogo["rodando"]:
        tempo_decorrido = relogio.tick(FPS) / 1000

        tratar_eventos(jogo, participantes)

        mouse = pygame.mouse.get_pos()
        tela.fill(AZUL_NOTURNO)

        if jogo["estado"] == "menu":
            desenhar_menu(tela, fonte_titulo)
        elif jogo["estado"] == "jogando":
            atualizar_partida(jogo, participantes, mouse, tempo_decorrido)
            desenhar_partida(tela, fonte_nome, fonte_pista, jogo, participantes, mouse)
        elif jogo["estado"] == "vitoria":
            desenhar_fim(tela, fonte_titulo, "Você achou a IA!")
        elif jogo["estado"] == "derrota":
            desenhar_fim(tela, fonte_titulo, "Fim de jogo")

        pygame.display.flip()

    pygame.quit()
