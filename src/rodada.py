import random


from src.config import PISTAS_IA, PISTAS_HUMANO


def preparar_rodada(participantes):
    """
    Prepara uma rodada nova: sorteia quem é a IA e distribui as pistas.

    Parâmetros:
        participantes (list): lista de Participante da rodada

    Informações relevantes:
        Não devolve nada: altera os próprios objetos da lista
        Primeiro limpa tudo da rodada anterior, depois sorteia
        Cada participante recebe pistas do grupo certo (IA ou humano)
        random.sample sorteia sem repetir; shuffle embaralha a ordem em que
        as pistas serão reveladas
    """
    # limpa o estado da rodada anterior
    for p in participantes:
        p.eh_ia = False
        p.pistas_reveladas = []
        p.pistas_disponiveis = []


    ia = random.choice(participantes)
    ia.eh_ia = True

    # distribuir as pistas entre os participantes da rodada 
    for p in participantes:
        if p.eh_ia:
            pistas = random.sample(PISTAS_IA, 5)
        else:
            pistas = random.sample(PISTAS_HUMANO, 5)
        random.shuffle(pistas)
        p.pistas_disponiveis = pistas