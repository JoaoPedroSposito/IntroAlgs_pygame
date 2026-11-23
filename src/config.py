# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
# tela
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Quem é a IA?"

# jogador
VIDAS_INICIAIS = 3

# objetos
RAIO_LUPA = 25
TEMPO_ESCANEAMENTO = 1.5
RAIO_PARTICIPANTE = 30

# pistas 
PISTAS_IA = ["escrita bem formal entre amigos",
             "não fala nada pessoal",
             "Reformulou a ideia do grupo em vez de dar opinião própria",
             "online há 10 h seguidas",
             "usa gírias fora de contexto",
             ]
PISTAS_HUMANO = ["costuma errar na digitação", 
                 "cita experiências pessoais",
                 "usa gírias e abreviações",
                 "faz pausas entre as mensagens",
                 "responde em 4 s",
                 ]

# fontes 
TAMANHO_FONTE_TITULO = 48
TAMANHO_FONTE_NOME = 24
TAMANHO_FONTE_PISTA = 22

# painel de pistas
LARGURA_PAINEL = 200
LIMITE_LINHA_PAINEL = 24

# cores 
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212,212,212)       
AZUL_NOTURNO = (0, 0, 30) 
AZUL_PAINEL = (15, 15, 60)
CINZA_MUDO = (90, 90, 90)

# arquivos
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"