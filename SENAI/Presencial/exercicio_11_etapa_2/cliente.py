class Cliente:
    def __init__(self, nome=None):
        self.nome = nome  # Atributo nome do cliente
        self.clientes = []  # Lista de clientes será inicializada no __init__

    def adicionar_cliente(self, nome_cliente):
        novo_cliente = Cliente(nome_cliente)  # Instanciando um novo cliente
        self.clientes.append(novo_cliente)  # Adicionando o cliente à lista
        print(f"Cliente {nome_cliente} adicionado com sucesso!")

    def deletar_cliente(self, nome_cliente):
        # Localizando o índice do cliente pelo nome
        indice_cliente = next((i for i, cliente in enumerate(self.clientes) if cliente.nome == nome_cliente), None)
        if indice_cliente is not None:
            self.clientes.pop(indice_cliente)  # Removendo o cliente pela posição na lista
            print(f"Cliente {nome_cliente} deletado com sucesso!")
        else:
            print(f"Cliente {nome_cliente} não encontrado!")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        for i, cliente in enumerate(self.clientes):
            print(f"{i} - Cliente: {cliente.nome}")