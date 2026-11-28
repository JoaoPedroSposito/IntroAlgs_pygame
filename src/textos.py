def quebrar_texto(texto, fonte, largura_max):
    """
    Divide um texto em linhas que cabem na largura dada.

    Parâmetros:
        texto (str): texto completo
        fonte (pygame.font.Font): fonte usada para medir a largura
        largura_max (int): largura máxima de cada linha, em pixels

    Retorno:
        list: lista de linhas (str)
    """
    linhas = []
    linha_atual = ""
    for palavra in texto.split(" "):
        if linha_atual == "":
            teste = palavra
        else:
            teste = linha_atual + " " + palavra
        if fonte.size(teste)[0] <= largura_max:
            linha_atual = teste               # coube: continua na mesma linha
        else:
            linhas.append(linha_atual) 
            linha_atual = palavra
    linhas.append(linha_atual)       
    return linhas