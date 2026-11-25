from src.rodada import preparar_rodada
from src.participante import Participante


def test_preparar_rodada_tem_uma_ia():
    participantes = [Participante(n, 0, 0, (0, 0, 0)) for n in ("A", "B", "C", "D")]
    preparar_rodada(participantes)
    assert sum(p.eh_ia for p in participantes) == 1    # True conta como 1


def test_todos_tem_pistas_disponiveis():
    participantes = [Participante(n, 0, 0, (0, 0, 0)) for n in ("A", "B", "C", "D")]
    preparar_rodada(participantes)
    assert all(len(p.pistas_disponiveis) >= 2 for p in participantes)

