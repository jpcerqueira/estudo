class Pedido:
    def __init__(self):
        self.pedidos = {}

    def adicionar_pedido(self, item, quantidade):
        if item in self.pedidos:
            self.pedidos[item] += quantidade
        else:
            self.pedidos[item] = quantidade

    def calcular_total(self, cardapio):
        total:float = 0
        for item, quantidade in self.pedidos.items():
            if item in cardapio.itens:
                total += cardapio.itens[item] * quantidade
        return total
    
    def mostrar_pedidos(self):
        for nome, quantidade in self.pedidos.items():
            print(f'{nome}: {quantidade} unidade(s)')
        print()