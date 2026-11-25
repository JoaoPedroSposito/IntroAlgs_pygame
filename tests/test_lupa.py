from src.lupa import Lupa
from src.participante import Participante



def test_escaneamento_completa_em_1_5_segundos():
    lupa = Lupa()
    ana = Participante("Ana", 0, 0, (0, 0, 0))
    assert lupa.atualizar(ana, 1.0) is False   # primeiro frame só define o alvo
    assert lupa.atualizar(ana, 1.0) is False   # escaneando a 1.0s faltando 0.5s
    assert lupa.atualizar(ana, 0.6) is True    # 1,6s, passou de 1,5s

def test_trocar_de_alvo_zera_o_progresso():
    lupa = Lupa()
    ana = Participante("Ana", 0, 0, (0, 0, 0))
    leo = Participante("Léo", 100, 0, (0, 0, 0))
    lupa.atualizar(ana, 1.0)
    lupa.atualizar(leo, 0.6)    # trocou de alvo: não soma, zera
    assert lupa.progresso == 0
    assert lupa.escaneando is leo