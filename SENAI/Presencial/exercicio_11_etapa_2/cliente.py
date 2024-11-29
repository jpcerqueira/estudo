class Cliente:
    def __init__(self, nome:str = ''):
        self.nome = nome
        self.clientes = []

    def adicionar_cliente(self, nome:str):
        if nome == '':
            print(f'O nome não pode ser vazio!')
            return
        for cliente in self.clientes:
            if cliente.nome == nome:
                print(f'Cliente {nome} já existe na lista!')
                return
        novo_cliente = Cliente(nome)
        self.clientes.append(novo_cliente)
        print(f'Cliente {nome} adicionado com sucesso!')

    def deletar_cliente(self, nome:str): #ver como não executar função qdo lista tiver vazia, talvez tenha que ser no main
        if nome == '':
            print(f'O nome não pode ser vazio!')
            return
        for cliente in self.clientes:
            if cliente.nome == nome:
                self.clientes.remove(cliente)
                print(f'Cliente {nome} deletado com sucesso!')
                return      
        print(f'Cliente {nome} não encontrado!')

    def listar_clientes(self):
        if not self.clientes:
            print('Nenhum cliente cadastrado.')
        else:
            for i, cliente in enumerate(self.clientes):
                print(f'{i} - Nome: {cliente.nome}') #rever se é necessário indice