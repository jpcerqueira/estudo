class Cardapio:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, nome, preco):
        self.itens[nome] = preco

    def remover_item(self, nome):
        if nome in self.itens:
            del self.itens[nome]

    def mostrar_cardapio(self):
        for nome, preco in self.itens.items():
            print(f'{nome}: R$ {preco:.2f}')
        print()