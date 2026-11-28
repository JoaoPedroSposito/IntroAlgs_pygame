from src.participante import Participante
from src.rodada import preparar_rodada
from src.dialogo import Dialogo


def criar_rodada():
    """Monta 4 participantes, prepara a rodada e inicia o diálogo."""
    participantes = [Participante(n, 0, 0, (0, 0, 0)) for n in ("A", "B", "C", "D")]
    preparar_rodada(participantes)
    dialogo = Dialogo()
    dialogo.iniciar(participantes)
    return participantes, dialogo

def test_ia_fica_no_papel_a_ou_b():
    """A IA sempre ocupa o papel A ou B."""
    participantes, dialogo = criar_rodada()
    ia = [p for p in participantes if p.eh_ia][0]
    assert dialogo.participantes["A"] is ia or dialogo.participantes["B"] is ia

def test_todas_as_falas_saem_na_ordem():
    """Com tempo de sobra, saem 12 falas, uma por chamada, e depois None."""
    participantes, dialogo = criar_rodada()
    falas = []
    for i in range(12):
        resultado = dialogo.atualizar(100)
        assert resultado is not None
        falas.append(resultado)
    assert dialogo.atualizar(100) is None
    assert falas[0][0] is dialogo.participantes[dialogo.ordem[0]]