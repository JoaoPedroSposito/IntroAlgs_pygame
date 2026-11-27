import random


from src.config import PISTAS_IA, PISTAS_HUMANO


def preparar_rodada(participantes):
    """
    Prepara uma rodada nova: sorteia quem é a IA e distribui as pistas.

    Parâmetros:
        participantes (list): lista de Participante da rodada
    """
    # limpa o estado da rodada anterior
    for p in participantes:
        p.eh_ia = False
        p.pistas_reveladas = []
        p.pistas_disponiveis = []

    ia = random.choice(participantes) # Escolhe um
    ia.eh_ia = True

    pistas_ia = PISTAS_IA.copy()
    pistas_humano = PISTAS_HUMANO.copy()

    # distribuir as pistas entre os participantes da rodada
    for p in participantes:
        if p.eh_ia:
            pistas = random.sample(pistas_ia, 2)
            for pista in pistas:
                pistas_ia.remove(pista)
        else:
            pistas = random.sample(pistas_humano, 2)
            for pista in pistas:
                pistas_humano.remove(pista)
        random.shuffle(pistas)   # Embaralha 
        p.pistas_disponiveis = pistas

def calcular_pontos(valor_barra, acertou):
    """
    Calcula a pontuação da partida.

    Parâmetros:
        valor_barra (float): influência da IA no momento da acusação (0 a 100)
        acertou (bool): True se o jogador acusou a IA certa

    Retorno:
        int: pontos da partida (0 se errou
    """
    if not acertou:
        return 0
    return int((100 - valor_barra) * 10)