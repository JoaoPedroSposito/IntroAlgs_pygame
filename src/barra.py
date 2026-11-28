import random

from src.config import BARRA_MAXIMO, ATRASO_BARRA


class BarraInfluencia:
    """
    Barra que mede a influência da IA sobre o grupo. Quando enche, o jogador perde.

    Atributos:
        valor (float): quanto a barra tem agora, de 0 até BARRA_MAXIMA
        fila (list): subidas que ainda não chegaram; cada item é [segundos_restantes, quantidade]
    """

    def __init__(self):
        self.valor_atual = 0
        self.fila_aumento = []

    def subir(self, quantidade):
        """Agenda uma subida: ela só chega depois de um prazo aleatório."""
        prazo = random.uniform(ATRASO_BARRA[0], ATRASO_BARRA[1])
        self.fila_aumento.append([prazo, quantidade])


    def subir_escaneamento(self, quantidade):
        """Sobe a barra na hora, sem atraso."""
        self.valor_atual += quantidade
        if self.valor_atual > BARRA_MAXIMO:
            self.valor_atual = BARRA_MAXIMO

    def atualizar(self, tempo_decorrido):
        """Chamada a cada frame: diminui o prazo de cada subida e aplica as que chegaram."""
        ainda_esperando = []                     
        for item in self.fila_aumento:
            item[0] -= tempo_decorrido     # item[0] é o prazo: diminui o tempo que passou
            if item[0] <= 0:
                self.valor_atual += item[1]     # item[1] é a quantidade: chegou, entra na barra
            else:
                ainda_esperando.append(item)    # ainda não chegou, continua esperando
        self.fila_aumento = ainda_esperando               
        if self.valor_atual > BARRA_MAXIMO:
            self.valor_atual = BARRA_MAXIMO          

    def encheu(self):
        """Devolve True se a barra chegou ao máximo."""
        return self.valor_atual >= BARRA_MAXIMO