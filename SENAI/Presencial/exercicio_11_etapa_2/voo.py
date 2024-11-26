from aviao import Aviao

class Voo:
    def __init__(self):
        self.voos = []

    def criar_voo(self, aviao: Aviao, origem: str, destino: str):
        numero_voo = len(self.voos) + 1
        voo = {"numero": numero_voo, "aviao": aviao, "origem": origem, "destino": destino, "reservas": []}
        self.voos.append(voo)
        print(f"Voo {numero_voo} criado com sucesso.")

    def deletar_voo(self, idx_voo: int):
        if 0 <= idx_voo < len(self.voos):
            self.voos.pop(idx_voo)
            print(f"Voo {idx_voo + 1} deletado com sucesso.")
        else:
            print("Voo não encontrado.")

    def listar_voos(self):
        if not self.voos:
            print("Nenhum voo cadastrado.")
        for i, voo in enumerate(self.voos):
            print(f"{i} - Voo {voo['numero']} de {voo['origem']} para {voo['destino']}")