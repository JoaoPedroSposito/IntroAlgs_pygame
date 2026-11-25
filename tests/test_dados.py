from src.dados import carregar_json


def test_carregar_json(tmp_path):
    """Lê um JSON gravado numa pasta temporária e devolve o mesmo conteúdo."""
    arquivo = tmp_path / "teste.json"
    arquivo.write_text('{"nome": "Ana", "pistas": ["olá"]}', encoding="utf-8")
    assert carregar_json(arquivo) == {"nome": "Ana", "pistas": ["olá"]}
