import pygame
from src.config import (
    BRANCO,
    RAIO_PARTICIPANTE,
    CINZA_MUDO
)


class Participante:
    def __init__(self,nome, x, y, cor):
        self.nome = nome
        self.x = x
        self.y = y
        self.cor = cor
        self.eh_ia = False
        self.raio = RAIO_PARTICIPANTE
        self.pistas_reveladas = []
        self.pistas_disponiveis = []
        self.mudo = False

    def revelar_pista(self):
        if self.mudo or len(self.pistas_disponiveis) == 0:
            return False

    def desenhar(self, tela, fonte):
        cor = CINZA_MUDO if self.mudo else self.cor
        pygame.draw.circle(tela, cor, (self.x, self.y), self.raio)

    def desenhar(self, tela, fonte):
        pygame.draw.circle(tela, self.cor, (self.x, self.y), self.raio)
        surface = fonte.render(self.nome, True, BRANCO)
        retangulo = surface.get_rect(center=(self.x, self.y + self.raio + 20))
        tela.blit(surface, retangulo)

    def esta_sob(self, mouse):
        # distancia entre o mouse e o centro do participante
        # x é horizontal e y é vertical
        distancia_x = mouse[0] - self.x
        distancia_y = mouse[1] - self.y
        return distancia_x * distancia_x + distancia_y * distancia_y <= self.raio * self.raio

    def revelar_pista(self):
        if len(self.pistas_disponiveis) == 0:
            return False
        self.pistas_reveladas.append(self.pistas_disponiveis.pop(0))
        return True    

        