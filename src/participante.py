import pygame


from src.config import (
    BRANCO,
    LADO_PARTICIPANTE,
)


class Participante:
    def __init__(self,nome, x, y, cor):
        self.nome = nome
        self.cor = cor
        self.rect = pygame.Rect(0, 0, LADO_PARTICIPANTE, LADO_PARTICIPANTE)
        self.rect.center = (x, y)
        self.eh_ia = False
        self.pistas_reveladas = []
        self.pistas_disponiveis = []
        self.iamgem = None
        self.mensagem_atual = None
        self.tempo_balao = 0

    def desenhar(self, tela, fonte):
        pygame.draw.rect(tela, self.cor, self.rect)
        surface = fonte.render(self.nome, True, BRANCO)
        retangulo = surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 20))
        tela.blit(surface, retangulo)

    def esta_sob(self, mouse):
        return self.rect.collidepoint(mouse)
    

    def revelar_pista(self):
        if len(self.pistas_disponiveis) == 0:
            return False
        self.pistas_reveladas.append(self.pistas_disponiveis.pop(0))
        return True    

        