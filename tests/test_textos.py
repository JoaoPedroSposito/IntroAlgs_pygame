import pygame


from src.textos import quebrar_texto


def test_quebrar_texto_cabe_na_largura():
    """Nenhuma linha passa da largura máxima e nenhuma palavra se perde."""
    pygame.font.init()
    fonte = pygame.font.Font(None, 22)
    texto = "reformulou a ideia do grupo em vez de dar opinião própria"
    linhas = quebrar_texto(texto, fonte, 150)
    assert all(fonte.size(linha)[0] <= 150 for linha in linhas)
    assert " ".join(linhas) == texto