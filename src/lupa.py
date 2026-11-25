from src.config import TEMPO_ESCANEAMENTO


class Lupa:
    def __init__(self, tempo_escaneamento=TEMPO_ESCANEAMENTO):
        self.tempo_escaneamento = tempo_escaneamento
        self.escaneando = None
        self.progresso = 0

    def atualizar(self, escaneando, tempo_decorrido):
        """
        Atualiza o progresso do escaneamento. Chamada uma vez por frame.

        Parâmetros:
            escaneando (Participante ou None): quem está sob a lupa neste frame
            tempo_decorrido (float): segundos desde o frame anterior (dt)

        Retorno:
            bool: True no frame em que o escaneamento completa, senão False
        """
        if escaneando is not None and escaneando is self.escaneando:
            self.progresso += tempo_decorrido
        else:
            self.escaneando = escaneando
            self.progresso = 0

        if self.progresso >= self.tempo_escaneamento:
            self.progresso = 0
            return True
        return False
        