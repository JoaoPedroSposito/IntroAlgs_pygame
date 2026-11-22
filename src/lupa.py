class Lupa:
    def __init__(self, tempo_escaneamento=1.5):
        self.tempo_escaneamento = tempo_escaneamento
        self.escaneando = None
        self.progresso = 0

    def atualizar(self, escaneando, tempo_decorrido):
        if escaneando is not None and escaneando is self.escaneando:
            self.progresso += tempo_decorrido
        else:
            self.escaneando = escaneando
            self.progresso = 0

        if self.progresso >= self.tempo_escaneamento:
            self.progresso = 0
            return True
        return False
        