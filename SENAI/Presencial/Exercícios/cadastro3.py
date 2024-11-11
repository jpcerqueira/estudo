class Cadastro: # para criar a class e dar o nome dela
    def __init__(self, nome, idade): # função que funciona dentro da classe é chamada de método # os self, não precisa ser esse nome, é um parametro quase que obrigatorio em ter num metodo
        self.nome = nome # são os atributos
        self.idade = idade # o self é necessário para acessar um parâmetro da classe, por exemplo self.idade é o parametro idade da classe cadastro, podendo assim o usuario mudar e acessar esse valor do parametro, onde na função não é possivel
        #self.email = ""
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Índice: " # a classe irá retornar os dados usuário em forma de string
    def buscar(self, buscar_nome):
        if buscar_nome.lower() == self.nome.lower():  # comparando os nomes de forma case-insensitive
            return True
        return False



#colocar uma função? com uma condição para ver se foi lido um dado de entrada, caso não seja, mostrar na tela que não foi digitado um valor
#ex: if 'variavel': -> se a variavel estiver preenchida faça
#ou if 'variavel' == '' ou 0: -> se a variavel não tiver preenchida, só com a entrada vazia que fica as aspas ou 0, faça ## mas tomar cuidado pois o numero de entrada pode ser realmente zero

qtd = int(input("Quantos usuários serão cadastrados?"))
menu = 0
#usuario = cadastro()
usuarios = [] #aqui irei armazenar a classe
while (menu != 4):
    print("-----------------------------")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Localizar usuário")
    print("4 - Sair do Sistema")
    print("-----------------------------")
    menu = int(input())
    if (menu == 1):
        if (len(usuarios) < qtd):                 # condição atraves pela quantidade de itens na lista por quantidade definida pelo usuário no início do programa
            usuario = Cadastro(input("Nome do usuário:"), int(input("Idade do usuário:")))     # atribuição a variavel usuario
            usuarios.append(usuario)                # adiciona a variavel usuario ao vetor usuarios atraves do metodo append
        else:
            print("Número de cadastros completo.")
    if (menu == 2):
        if (len(usuarios) == 0):
            print("Nenhum usuário cadastrado.")
        else:
            for indice, i in enumerate(usuarios): #enumerate da o indice e o valor de um vetor, mas como o vetor esta armazenando uma class, temos que usar o def __STR__ para apresentar cmo string
                print(i, indice)
    if (menu == 3):
        buscar_nome = input("Digite o nome do usuário a ser encontrado: ")
        encontrado = False
        for indice, usuario in enumerate(usuarios):
            if usuario.buscar(buscar_nome):  # usando o método buscar da classe
                print(f"Usuário encontrado: {usuario}", indice)
                encontrado = True
                break
        if not encontrado:
            print("Usuário não encontrado.")
print("Fim do Programa")