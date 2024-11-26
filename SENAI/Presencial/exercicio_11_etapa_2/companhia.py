from aviao import Aviao

class Companhia:
    def __init__(self):
        self.avioes = []

    def adicionar_aviao(self, identificacao: str, total_assentos: int):
        aviao = Aviao(identificacao, total_assentos)
        self.avioes.append(aviao)
        print(f"Avião {identificacao} cadastrado com sucesso.")

    def deletar_aviao(self, identificacao: str):
        for aviao in self.avioes:
            if aviao.identificacao == identificacao:
                self.avioes.remove(aviao)
                print(f"Avião {identificacao} deletado com sucesso.") #a ver
                return
        print("Avião não encontrado.")

    def listar_avioes(self):
        if not self.avioes:
            print("Nenhum avião cadastrado.")
        for i, aviao in enumerate(self.avioes):
            print(f"{i} - {aviao}")