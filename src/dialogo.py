import random

from src.dados import carregar_json
from src.config import CAMINHO_DIALOGOS, ATRASO_HUMANO, ATRASO_IA


class Dialogo:
    """
    Controla a conversa do chat: quem fala, o que fala e quando.

    Atributos:
        dialogos (list): todos os diálogos lidos do JSON
        assunto (str): assunto do diálogo sorteado
        ordem (list): ordem dos papéis falando, por exemplo ["A", "B", ...]
        falas (dict): papel -> lista de falas (já na versão humana ou de IA)
        participantes (dict): papel -> Participante que representa esse papel
        usadas (dict): papel -> quantas falas desse papel já foram ditas
        indice (int): posição atual dentro de "ordem"
        espera (float): segundos que faltam para a próxima fala
    """

    def __init__(self):
        self.dialogos = carregar_json(CAMINHO_DIALOGOS)
        self.anterior = None
        self.assunto = ""
        self.ordem = []
        self.falas = {}
        self.participantes = {}
        self.usadas = {}
        self.indice = 0
        self.espera = 0

    def sortear_espera(self):
        """Sorteia quanto tempo falta para a próxima fala, conforme quem vai falar."""
        papel = self.ordem[self.indice]
        if self.participantes[papel].eh_ia:
            return random.uniform(ATRASO_IA[0], ATRASO_IA[1])
        return random.uniform(ATRASO_HUMANO[0], ATRASO_HUMANO[1])

    def iniciar(self, participantes):
        """
        Começa um diálogo novo. Deve ser chamada depois de preparar_rodada.

        Parâmetros:
            participantes (list): os 4 Participante, um deles já marcado como IA

        Informações relevantes:
            A IA recebe o papel A ou B (sorteado); os outros 3 papéis vão
            para os humanos em ordem aleatória
            O papel de IA usa a versão "ia" das falas; os demais, a "humano"
        """
        # escolhe um diálogo diferente do anterior (se houver mais de um)
        opcoes = [d for d in self.dialogos if d is not self.anterior]
        if len(opcoes) == 0:
            opcoes = self.dialogos
        escolhido = random.choice(opcoes)
        self.anterior = escolhido

        self.assunto = escolhido["assunto"]
        self.ordem = escolhido["ordem"]

        ia = [p for p in participantes if p.eh_ia][0]
        humanos = [p for p in participantes if not p.eh_ia]
        random.shuffle(humanos)
        papel_ia = random.choice(["A", "B"])

        self.participantes = {}
        self.falas = {}
        self.usadas = {}
        for papel in ["A", "B", "C", "D"]:
            if papel == papel_ia:
                self.participantes[papel] = ia
                versao = "ia"
            else:
                self.participantes[papel] = humanos.pop()
                versao = "humano"
            self.falas[papel] = escolhido["papeis"][papel][versao]
            self.usadas[papel] = 0

        self.indice = 0
        self.espera = self.sortear_espera()

    def atualizar(self, tempo_decorrido):
        """
        Faz o tempo passar. Chamada uma vez por frame.

        Parâmetros:
            tempo_decorrido (float): segundos desde o frame anterior (dt)

        Retorno:
            tuple ou None: (participante, texto) no frame em que alguém fala,
            senão None
        """
        if self.indice >= len(self.ordem):
            return None                                   # o diálogo acabou
        self.espera -= tempo_decorrido
        if self.espera > 0:
            return None                                   # ainda não é hora

        papel = self.ordem[self.indice]
        texto = self.falas[papel][self.usadas[papel]]
        participante = self.participantes[papel]
        self.usadas[papel] += 1
        self.indice += 1
        if self.indice < len(self.ordem):
            self.espera = self.sortear_espera()
        return participante, texto