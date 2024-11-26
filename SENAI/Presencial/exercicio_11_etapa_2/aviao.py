class Aviao:
    def __init__(self, identificacao: str, total_assentos: int):
        self.identificacao = identificacao
        self.total_assentos = total_assentos

    def __str__(self):
        return f"Avião: {self.identificacao}, Assentos: {self.total_assentos}"