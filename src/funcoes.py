def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def quebrar_texto(texto, limite):
    """Divide o texto em linhas com no máximo `limite` caracteres."""
    linhas = []
    linha = ""
    for palavra in texto.split():
        if linha == "":
            linha = palavra
        elif len(linha) + 1 + len(palavra) <= limite:
            linha = linha + " " + palavra
        else:
            linhas.append(linha)
            linha = palavra
    if linha != "":
        linhas.append(linha)
    return linhas