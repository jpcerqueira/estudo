class Pedido:
    def __init__(self):
        self.item = None
        self.quantidade = 0
        self.pedido_atual = []
        self.pedidos = []

    def adicionar_item(self, item, quantidade):
        self.item = item
        self.quantidade = quantidade
        self.pedido_atual.append({"item": self.item, "quantidade": self.quantidade})

    def finalizar_pedido(self):
        self.pedidos.append(self.pedido_atual)
        self.pedido_atual = []

    def calcular_total_por_indice(self, indice, cardapio):
        if 0 <= indice < len(self.pedidos):
            total = 0
            pedido = self.pedidos[indice]
            for item_pedido in pedido:
                item = item_pedido['item']
                quantidade = item_pedido['quantidade']
                if item in cardapio.itens:
                    total += cardapio.itens[item] * quantidade
            return total
        else:
            print("Índice de pedido inválido.")
            return 0

    def mostrar_todos_pedidos(self):
        print('Todos os Pedidos:')
        for i, pedido in enumerate(self.pedidos, start=1):
            print(f'Pedido {i}:')
            for item_pedido in pedido:
                print(f'  {item_pedido["item"]}: {item_pedido["quantidade"]} unidade(s)')
            print()
