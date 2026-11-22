from src.participante import Participante
from src.lupa import Lupa

def test_esta_sob():
    p1 = Participante("Ana", 100, 100, (255, 0, 0))
    assert p1.esta_sob((100, 100)) == True
    assert p1.esta_sob((120, 110)) == True
    assert p1.esta_sob((500, 500)) == False

def test_escaneamento_completa_em_1_5_segundos():
    lupa = Lupa()
    ana = Participante("Ana", 0, 0, (0, 0, 0))
    assert lupa.atualizar(ana, 1.0) is False
    assert lupa.atualizar(ana, 1.0) is False
    assert lupa.atualizar(ana, 0.6) is True

def test_trocar_de_alvo_zera_o_progresso():
    lupa = Lupa()
    ana = Participante("Ana", 0, 0, (0, 0, 0))
    leo = Participante("Léo", 100, 0, (0, 0, 0))
    lupa.atualizar(ana, 1.0)
    lupa.atualizar(leo, 0.6)
    assert lupa.progresso == 0
    assert lupa.escaneando is leo