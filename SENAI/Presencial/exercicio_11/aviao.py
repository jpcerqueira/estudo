class Aviao:
    def __init__(self, identificacao, total_assentos):
        self.identificacao = identificacao
        self.total_assentos = total_assentos

    def __str__(self):
        return f'Avião ID: {self.identificacao}, Assentos: {self.total_assentos}'