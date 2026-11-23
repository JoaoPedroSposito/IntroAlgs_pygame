import random
from src.config import PISTAS_IA, PISTAS_HUMANO
from src.funcoes import tomar_dano


def preparar_rodada(participantes):
    # limpa o estado da rodada anterior
    for p in participantes:
        p.eh_ia = False
        p.mudo = False
        p.pistas_reveladas = []
        p.pistas_disponiveis = []


    ia = random.choice(participantes)
    ia.eh_ia = True

    # distribuir as pistas entre os participantes da rodada 
    for p in participantes:
        if p.eh_ia:
            pistas = random.sample(PISTAS_IA, 2)
        else:
            pistas = random.sample(PISTAS_HUMANO, 2)
        random.shuffle(pistas)
        p.pistas_disponiveis = pistas


def acusar(acusado, vidas):
    # retorna se acertou e as vidas restantes; quem foi acusado errado fica mudo
    if acusado.eh_ia:
        return True, vidas
    acusado.mudo = True
    return False, tomar_dano(vidas, 1)
