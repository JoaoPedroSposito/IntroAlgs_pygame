from src.participante import Participante
from src.lupa import Lupa
from src.rodada import preparar_rodada

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

def test_preparar_rodada_tem_uma_ia():
    participantes = [Participante(n, 0, 0, (0, 0, 0)) for n in ("A", "B", "C", "D")]
    preparar_rodada(participantes)
    assert sum(p.eh_ia for p in participantes) == 1

def test_todos_tem_pistas_disponiveis():
    participantes = [Participante(n, 0, 0, (0, 0, 0)) for n in ("A", "B", "C", "D")]
    preparar_rodada(participantes)
    assert all(len(p.pistas_disponiveis) >= 2 for p in participantes)

def test_revelar_pista():
    ana = Participante("Ana", 0, 0, (0, 0, 0))
    ana.pistas_disponiveis = ["pista 1", "pista 2"]
    assert ana.revelar_pista() is True
    assert ana.pistas_reveladas == ["pista 1"]
    assert ana.revelar_pista() is True
    assert ana.revelar_pista() is False
    assert ana.pistas_reveladas == ["pista 1", "pista 2"]