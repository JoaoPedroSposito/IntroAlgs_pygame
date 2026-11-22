from src.participante import Participante

def test_esta_sob():
    p1 = Participante("Ana", 100, 100, (255, 0, 0))
    assert p1.esta_sob((100, 100)) == True
    assert p1.esta_sob((120, 110)) == True
    assert p1.esta_sob((500, 500)) == False