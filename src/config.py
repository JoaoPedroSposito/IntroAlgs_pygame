# Configurações centrais do jogo (tela, objetos, painel, cores e caminhos).

# tela
LARGURA_TELA = 960
ALTURA_TELA = 640
FPS = 60
TITULO_JOGO = "Quem é a IA?"

# fontes
TAMANHO_FONTE_TITULO = 48
TAMANHO_FONTE_NOME = 28

# objetos
RAIO_LUPA = 25
TEMPO_ESCANEAMENTO = 1.5
LADO_PARTICIPANTE = 100

# barra de nfluencia
BARRA_MAXIMO = 100
ATRASO_BARRA = (2.5, 4.0)
AUMENTO_ESCANEAMENTO = 15
AUMENTO_MENSAGEM_IA = 10 
# visual barra 
BARRA_X = 260
BARRA_Y = 50
BARRA_LARGURA = 400
BARRA_ALTURA = 20
COR_BARRA = (255, 200, 0)
COR_FUNDO_BARRA = (60, 60, 80)

# dialogo
CAMINHO_DIALOGOS = "data/dialogos.json"
ATRASO_HUMANO = (2.5, 5.0)     
ATRASO_IA = (0.5, 4.0)         
DURACAO_BALAO = 6              
LARGURA_BALAO = 185 
LARGURA_ASSUNTO = 150       

# painel de pistas
PAINEL_X = 700
PAINEL_LARGURA = LARGURA_TELA - PAINEL_X
COR_PAINEL = (19, 34, 62)
TAMANHO_FONTE_PISTA = 22
ESPACO_LINHA = 24
INDENTACAO_PISTA = 25
MARGEM_ESQUERDA = 15

# pistas
PISTAS_IA = ["escrita bem formal entre amigos",
             "não fala nada pessoal",
             "Reformulou a ideia do grupo em vez de dar opinião própria", # Pendente resolução da quebra de mensagem
             "online há 10 h seguidas",
             "usa gírias fora de contexto",
             ]
PISTAS_HUMANO = ["costuma errar na digitação",
                 "cita experiências pessoais",
                 "usa gírias e abreviações",
                 "faz pausas entre as mensagens",
                 "responde em 4 s",
                 "se corrige depois de errar uma palavra",
                 "demora minutos para responder",
                 "só aparece online à noite",
                 ]

# personagens
# (Pessoa 4) lista NOMES_AVATARES e tamanho dos avatares 

# cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)
AZUL_NOTURNO = (8, 14, 28)
COR_SUSPEITO = (220, 60, 60)

# arquivos
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"