from src.rodada import preparar_rodada, calcular_pontos
from src.participante import Participante


def test_preparar_rodada_tem_uma_ia():
    participantes = [Participante(n, 0, 0, (0, 0, 0)) for n in ("A", "B", "C", "D")]
    preparar_rodada(participantes)
    assert sum(p.eh_ia for p in participantes) == 1    # True conta como 1


def test_todos_tem_pistas_disponiveis():
    participantes = [Participante(n, 0, 0, (0, 0, 0)) for n in ("A", "B", "C", "D")]
    preparar_rodada(participantes)
    assert all(len(p.pistas_disponiveis) >= 2 for p in participantes)

def test_humanos_nao_repetem_pistas():
    """Duas pessoas humanas nunca recebem a mesma pista na mesma rodada."""
    participantes = [Participante(n, 0, 0, (0, 0, 0)) for n in ("A", "B", "C", "D")]
    preparar_rodada(participantes)
    pistas_humanas = []
    for p in participantes:
        if not p.eh_ia:
            pistas_humanas += p.pistas_disponiveis
    assert len(pistas_humanas) == len(set(pistas_humanas))

def test_calcular_pontos():
    """Acertar com a barra baixa vale mais; errar vale 0."""
    assert calcular_pontos(0, True) == 1000
    assert calcular_pontos(30, True) == 700
    assert calcular_pontos(30, False) == 0