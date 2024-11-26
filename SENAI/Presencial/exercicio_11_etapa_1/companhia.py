from aviao import Aviao

class Companhia:
    def __init__(self):
        self.avioes:list[Aviao] = []

    def adicionar_aviao(self, identificacao='', total_assentos=0):
        novo_aviao = Aviao(identificacao, total_assentos)
        self.avioes.append(novo_aviao)

    def listar_avioes(self):
        if not self.avioes:
            print('Nenhum avião cadastrado.')
        else:
            print('Lista de Aviões:')
            for aviao in self.avioes:
                print(aviao)
    