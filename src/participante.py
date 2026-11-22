import pygame
from src.config import (
    BRANCO,
    RAIO_PARTICIPANTE,
)


class Participante:
    def __init__(self,nome, x, y, cor):
        self.nome = nome
        self.x = x
        self.y = y
        self.cor = cor
        self.eh_ia = False
        self.pistas = []
        self.raio = RAIO_PARTICIPANTE

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


        