class Aviao:
    def __init__(self, identificacao='', total_assentos=0):
        self.identificacao:str = identificacao
        self.total_assentos:int = total_assentos

    def __str__(self):
        return f'Prefixo do Avião: {self.identificacao}, Assentos: {self.total_assentos}'