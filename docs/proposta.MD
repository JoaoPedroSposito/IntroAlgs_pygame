# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Quem é a IA?

## 2. Integrantes do grupo

- Nome 1: João Pedro Spósito Pereira Cézar
- Nome 2: Paulo Henrique De Souza Pereira
- Nome 3: Saul de Castro Macedo
- Nome 4: Tiago Belico de Oliveira e Silva

## 3. Tema escolhido

Conteúdos reais e artificiais: reconhecimento de sinais de textos gerados por IA e análise crítica dos resultados.

O objetivo do jogo é descobrir qual participante de um chat simulado é uma IA, interpretando sinais como tempo de resposta, texto genérico, ausência de experiência pessoal e padrões repetitivos. Como alguns humanos escrevem de forma formal e geram falsos suspeitos, nenhuma pista sozinha prova nada, e o jogador precisa cruzar informações. Acusar sem evidências suficientes gera penalidades, o que reforça a análise crítica e mostra que detectores e aparências também erram.

## 4. Tipo de jogo

Jogo de investigação e dedução em tempo real, com simulação básica de um chat. O jogador investiga participantes com uma lupa e age sob pressão de tempo.

## 5. Descrição geral do jogo

A tela mostra uma sala de chat com vários participantes (círculos com nome) soltando mensagens em balões. Um deles, sorteado a cada rodada, é uma IA disfarçada. O jogador controla uma lupa com o mouse: ao ficar sobre um participante por cerca de 1,5 s, a lupa escaneia e revela uma pista, que fica registrada em um bloco de notas lateral. Uma barra de “Influência da IA” sobe a cada mensagem da IA, e o jogador precisa identificá-la antes que a barra encha. Os desafios são o tempo limitado, a impossibilidade de investigar todos a tempo, os humanos “robóticos” que parecem IA e a IA que fica mais convincente a cada rodada.

## 6. Objetivo do jogador

Identificar a IA em cada rodada antes que sua influência chegue ao máximo, completando todas as rodadas com a maior pontuação possível.

## 7. Regras principais

- Regra 1: O jogador começa com 3 vidas e, a cada rodada, há exatamente uma IA entre os participantes, sorteada aleatoriamente.
- Regra 2: Manter a lupa sobre um participante por cerca de 1,5 s revela uma pista; as pistas ficam salvas no bloco de notas.
- Regra 3: A barra de Influência da IA sobe a cada mensagem da IA; se encher, a rodada é perdida.
- Regra 4: Acusar corretamente soma pontos (com bônus por tempo restante, por poucas pistas usadas e por combo de acertos seguidos).
- Regra 5: Acusar um humano retira uma vida, aumenta a influência da IA e deixa o participante inocente “mudo”, sem fornecer novas pistas.

## 8. Condição de vitória

Completar as 8 rodadas com pelo menos 1 vida restante.

## 9. Condição de derrota ou encerramento

A partida termina em derrota quando as vidas chegam a zero ou quando a barra de Influência da IA enche. Ao final (vitória ou derrota), é exibida uma tela com a pontuação, a posição no ranking e um resumo educativo dos erros cometidos.

## 10. Elementos previstos no jogo

Lupa controlada pelo mouse, que escaneia os participantes e revela pistas.
Tempo limitado, barra de influência da IA, humanos de escrita formal que geram falsos suspeitos e IA que se torna mais convincente nas rodadas finais.
Participantes do chat, balões de mensagem, bloco de notas com pistas, marcação de suspeito (bandeira vermelha) e power-ups opcionais (lupa rápida e congelar influência).
Pontuação com combo, 3 vidas, barra de influência da IA, tempo da rodada, indicador de rodada (ex.: 4/8) e ranking salvo em arquivo.

## 11. Controles previstos

Mouse: move a lupa. Manter a lupa parada sobre um participante: escaneia e revela pistas. Clique esquerdo: marca um participante como suspeito. Clique direito ou ESPAÇO: confirma a acusação. ESC: pausa ou volta ao menu.

## 12. Principais dificuldades esperadas

- Dificuldade 1: Controlar o tempo do escaneamento e da barra de influência de forma independente da taxa de quadros (uso de delta time).
- Dificuldade 2: Montar rodadas aleatórias equilibradas, garantindo sempre uma única IA e pistas que não revelem a resposta de forma óbvia.
- Dificuldade 3: Escrever conteúdo suficiente (mensagens e pistas) e organizar o trabalho em equipe e o uso do GitHub, separando lógica testável do código de interface.

## 13. Escopo mínimo para a entrega final

Uma tela com 4 participantes e uma lupa controlada pelo mouse, com escaneamento por tempo de permanência que revela pistas. Rodadas sorteadas a partir de um arquivo JSON (uma única IA por rodada), acusação com clique, 3 vidas, pontuação, barra de influência da IA, condições de vitória e derrota e ranking simples em arquivo de texto. Testes das funções de lógica (acusação, pontuação, influência e montagem da rodada).

## 14. Possíveis melhorias, caso haja tempo

- Melhoria 1: Aumentar para 8 participantes por rodada, com humanos “robóticos” para criar falsos suspeitos.
- Melhoria 2: Power-ups (lupa rápida e congelar influência) e combo de acertos seguidos.
- Melhoria 3: Efeitos visuais e sonoros, menu inicial e tela final com resumo educativo dos erros do jogador.
