# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

**Nome:**

Quem é a IA?

## 2. Integrantes do grupo

- Nome 1: João Pedro Spósito Pereira Cézar
- Nome 2: Paulo Henrique Pereira de Souza 
- Nome 3: Saul de Castro Macedo
- Nome 4: Tiago Belico de Oliveira e Silva

## 3. Tema escolhido

**Tema:**

Conteúdos reais e artificiais: reconhecimento de sinais de textos gerados por IA e análise crítica dos resultados.

**Como esse tema se relaciona com o jogo?**

O objetivo do jogo é descobrir qual participante de um chat simulado é uma IA, interpretando sinais como tempo de resposta, texto genérico, ausência de experiência pessoal e padrões repetitivos. Como alguns humanos escrevem de forma formal e geram falsos suspeitos, nenhuma pista sozinha prova nada, e o jogador precisa cruzar informações. Acusar sem evidências suficientes gera penalidades, o que reforça a análise crítica e mostra que detectores e aparências também erram.

## 4. Tipo de jogo

**Tipo escolhido:**

Jogo de investigação e dedução em tempo real, com simulação básica de um chat. O jogador investiga participantes com uma lupa e age sob pressão de tempo.

## 5. Descrição geral do jogo

**Descrição:**

A tela mostra uma sala de chat com vários participantes (círculos com nome) soltando mensagens em balões. Um deles, sorteado a cada rodada, é uma IA disfarçada. O jogador controla uma lupa com o mouse: ao ficar sobre um participante por cerca de 1,5 s, a lupa escaneia e revela uma pista, que fica registrada em um bloco de notas lateral. Uma barra de “Influência da IA” sobe a cada mensagem da IA, e o jogador precisa identificá-la antes que a barra encha. Os desafios são o tempo limitado, a impossibilidade de investigar todos a tempo, os humanos “robóticos” que parecem IA e a IA que fica mais convincente a cada rodada.

As informações vêm de duas fontes que precisam ser cruzadas: as mensagens do chat mostram o estilo de escrita de cada participante, e a lupa revela dados de comportamento, como tempo de resposta e horas online.

## 6. Objetivo do jogador

**Objetivo:**

Identificar a IA em cada rodada antes que sua influência chegue ao máximo, completando todas as rodadas com a maior pontuação possível.

## 7. Regras principais

- Regra 1: O jogador começa com 3 vidas e, a cada rodada, há exatamente uma IA entre os participantes, sorteada aleatoriamente.
- Regra 2: Manter a lupa sobre um participante por cerca de 1,5 s revela uma pista; as pistas ficam salvas no bloco de notas.
- Regra 3: A barra de Influência da IA sobe a cada mensagem da IA; se encher, o jogador perde 1 vida e a rodada recomeça com uma nova IA.
- Regra 4: Acusar corretamente soma pontos (com bônus por tempo restante e por poucas pistas usadas).
- Regra 5: Acusar um humano retira uma vida, aumenta a influência da IA e deixa o participante inocente “mudo”, sem fornecer novas pistas.

## 8. Condição de vitória

**Condição de vitória:**

Completar todas as rodadas (8 na versão completa e 3 na versão mínima) com pelo menos 1 vida restante.

## 9. Condição de derrota ou encerramento

**Condição de derrota ou encerramento:**

A partida termina em derrota quando as vidas chegam a zero. Quando a barra de Influência da IA enche, o jogador perde uma vida e a rodada recomeça com uma nova IA. Ao final (vitória ou derrota), é exibida uma tela com a pontuação, a posição no ranking e uma dica sobre o uso responsável de IA.

## 10. Elementos previstos no jogo

- **Personagem ou elemento principal:** A lupa controlada pelo mouse, que escaneia os participantes e revela pistas.
- **Obstáculos ou desafios:** Tempo limitado, barra de influência da IA, humanos de escrita formal que geram falsos suspeitos e IA que se torna mais convincente nas rodadas finais.
- **Itens ou objetos de interação (se houver):** Participantes do chat, balões de mensagem, bloco de notas com pistas, marcação de suspeito (bandeira vermelha) e power-ups opcionais (lupa rápida e congelar influência).
- **Pontuação, vidas, tempo ou progresso:** Pontuação, 3 vidas, barra de influência da IA, tempo da rodada, indicador de rodada (ex.: 4/8) e ranking salvo em arquivo.

## 11. Controles previstos

**Controles:**

Mouse: move a lupa. Manter a lupa parada sobre um participante: escaneia e revela pistas. Clique esquerdo: marca um participante como suspeito. Clique direito ou ESPAÇO: confirma a acusação. ESC: pausa ou volta ao menu.

## 12. Principais dificuldades esperadas

- Dificuldade 1: Controlar o tempo do escaneamento e da barra de influência de forma independente da taxa de quadros (uso de delta time).
- Dificuldade 2: Montar rodadas aleatórias equilibradas, garantindo sempre uma única IA e pistas que não revelem a resposta de forma óbvia.
- Dificuldade 3: Escrever conteúdo suficiente (mensagens e pistas) coerentes com o dialogo, e organizar o trabalho em equipe e o uso do GitHub, separando lógica testável do código de interface. As mensagens dos humanos serão escritas por nós do grupo, e as da IA serão geradas por um modelo de linguagem e atraves de comportamentos padrões de IA percebidos pelos integrantes do grupo.

## 13. Escopo mínimo para a entrega final

**Escopo mínimo:**

Versão inicial: uma tela com 4 participantes e uma lupa controlada pelo mouse, com escaneamento por tempo de permanência que revela pistas no bloco de notas. Uma rodada com uma única IA sorteada, acusação com clique, 3 vidas e condições de vitória e derrota. Testes das funções de lógica (escaneamento, sorteio da rodada, pistas e acusação).

Versão final: três rodadas sorteadas a partir de um arquivo JSON, pontuação, barra de influência da IA, tela final com a pontuação, a posição no ranking e uma dica fixa sobre o uso responsável de IA, e ranking simples em arquivo de texto.

## 14. Possíveis melhorias, caso haja tempo

- Melhoria 1: Aumentar para 8 participantes por rodada, com humanos “robóticos” para criar falsos suspeitos.
- Melhoria 2: Power-ups (lupa rápida e congelar influência) e combo de acertos seguidos.
- Melhoria 3: Efeitos visuais e sonoros e tela final com resumo educativo dos erros do jogador.