# Quem é a IA?

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- João Pedro Spósito Pereira Cézar
- Paulo Henrique De Souza
- Saul
- Tiago Belico

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Quatro participantes aparecem na tela e um deles, sorteado a cada partida, é uma IA disfarçada. O jogador usa uma lupa, controlada pelo mouse, para revelar pistas sobre cada participante e tenta descobrir quem é a IA.

## Objetivo do jogador

Acusar a IA antes de ficar sem vidas.

## Regras do jogo

- Há exatamente uma IA entre os participantes, sorteada no início da partida.
- O jogador começa com 3 vidas.
- Manter a lupa sobre um participante por 1,5 s revela uma pista, que aparece no painel lateral.
- Acusar a IA vence a partida.
- Acusar um humano tira 1 vida e deixa esse participante mudo: ele não revela mais pistas e não pode ser acusado de novo.
- Ao chegar a 0 vidas, o jogador perde.

## Controles

- Mouse: move a lupa.
- Clique esquerdo: acusa o participante sob o cursor.
- ENTER: inicia a partida no menu e volta ao menu na tela final.
- ESC: volta ao menu durante a partida e sai do jogo no menu.

## Como executar o projeto

```bash
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Versão inicial

Esta versão tem uma rodada por partida. Ainda não há pontuação, tempo, barra de influência da IA nem ranking, previstos em `docs/proposta.MD`.
