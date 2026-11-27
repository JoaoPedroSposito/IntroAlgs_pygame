import json


def carregar_json(caminho):
    """
    Lê um arquivo JSON e devolve o conteúdo já convertido para Python.

    Parâmetros:
        caminho (str): caminho do arquivo, por exemplo "data/pistas.json"

    Retorno:
        dict ou list: conteúdo do arquivo

    Informações relevantes:
        O arquivo é lido em UTF-8 para aceitar acentos
        Se o arquivo não existir, ocorre FileNotFoundError
    """
    
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)