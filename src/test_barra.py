from src.barra import BarraInfluencia


def test_subida_chega_depois_do_prazo():
    """A barra só sobe depois do prazo; depois de 10 s, a subida já chegou."""
    barra = BarraInfluencia()
    barra.subir(20)
    assert barra.valor_atual == 0          # recém agendada, ainda não chegou
    barra.atualizar(10)              # 10 s é mais que o prazo máximo (4 s)
    assert barra.valor_atual == 20