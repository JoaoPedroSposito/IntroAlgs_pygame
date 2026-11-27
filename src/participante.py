import pygame


from src.config import (
    BRANCO,
    LADO_PARTICIPANTE,
)


class Participante:
    def __init__(self,nome, x, y, cor):
        self.nome = nome
        self.cor = cor
        # o Rect nasce em (0, 0) com o tamanho do quadrado e depois é movido:
        # atribuir .center faz o meio do quadrado ficar em (x, y)
        self.rect = pygame.Rect(0, 0, LADO_PARTICIPANTE, LADO_PARTICIPANTE)
        self.rect.center = (x, y)
        self.eh_ia = False
        self.pistas_reveladas = []
        self.pistas_disponiveis = []
        self.imagem = None
        self.mensagem_atual = None
        self.tempo_balao = 0

    def desenhar(self, tela, fonte):
        """
        Desenha o quadrado colorido e o nome embaixo dele.

        Parâmetros:
            tela (pygame.Surface): janela onde será desenhado
            fonte (pygame.font.Font): fonte usada no nome
        """
        pygame.draw.rect(tela, self.cor, self.rect)
        if self.imagem is not None:
            tela.blit(self.imagem,self.rect)
        surface = fonte.render(self.nome, True, BRANCO)
        retangulo = surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 20))
        tela.blit(surface, retangulo)

    def esta_sob(self, mouse):
        """
        Diz se o mouse está dentro do quadrado do participante.

        Parâmetros:
            mouse (tuple): posição (x, y) do mouse na tela

        Retorno:
            bool: True se o ponto está dentro do quadrado
        """
        return self.rect.collidepoint(mouse)
    

    def revelar_pista(self):
        """
        Move a próxima pista de pistas_disponiveis para pistas_reveladas.

        Retorno:
            bool: True se revelou uma pista, False se não restava nenhuma

        Informações relevantes:
            pop(0) tira o PRIMEIRO item da lista e devolve ele,
            então as pistas saem na ordem em que foram sorteadas
        """
        if len(self.pistas_disponiveis) == 0:
            return False
        self.pistas_reveladas.append(self.pistas_disponiveis.pop(0))
        return True    

        