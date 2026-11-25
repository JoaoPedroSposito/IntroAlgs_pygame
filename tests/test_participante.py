from src.participante import Participante


def test_esta_sob():
    p1 = Participante("Ana", 100, 100, (255, 0, 0))
    assert p1.esta_sob((100, 100)) == True    # no centro do quadrado
    assert p1.esta_sob((120, 110)) == True    # dentro: o quadrado vai de 70 a 130
    assert p1.esta_sob((500, 500)) == False   # longe do quadrado

def test_revelar_pista():
    ana = Participante("Ana", 0, 0, (0, 0, 0))
    ana.pistas_disponiveis = ["pista 1", "pista 2"]
    assert ana.revelar_pista() is True
    assert ana.pistas_reveladas == ["pista 1"]
    assert ana.revelar_pista() is True
    assert ana.revelar_pista() is False    # não sobrou nenhuma
    assert ana.pistas_reveladas == ["pista 1", "pista 2"]