class cadastro: # para criar a class e dar o nome dela
    def __init__(self, nome, idade): # função quie funciona dentro da classe é chamada de método # os self, não precisa ser esse nome, é um parametro quase que obrigatorio em ter num metodo
        self.nome = nome # são os atributos
        self.idade = idade # o self é necessário para acessar um parâmetro da classe, por exemplo self.idade é o parametro idade da classe cadastro, podendo assim o usuario mudar e acessar esse valor do parametro, onde na função não é possivel
        #self.email = ""
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}" # a classe irá retornar os dados usuário em forma de string


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
            usuario = cadastro(input("Nome do usuário:"), int(input("Idade do usuário:")))     # atribuição a variavel usuario
            usuarios.append(usuario)                # adiciona a variavel usuario ao vetor usuarios atraves do metodo append
        else:
            print("Número de cadastros completo.")
    elif (menu == 2):
        if (len(usuarios) == 0):
            print("Nenhum usuário cadastrado.")
        else:
            for i in usuarios:
                print(i)
    elif menu == 3:
        localizar = input("Digite o nome do usuário que procura: ")
        encontrado = False #começa como falso para percorrer a lista e ver se tem ou não
        for i, usuario in enumerate(usuarios):  # percorre a lista para encontrar o nome atraves do vetor 'usarios'
            if usuario.nome == localizar: #localiza o usuario pelo nome atraves do nome dentro da variavel localizar
                print(f"Usuário encontrado no índice {i}: {usuario}")
                encontrado = True #se encontrar, encerra o loop
                break
        if not encontrado: # se não for encontrado, printa pois a 'not encontrado' sera verdadeiro
            print("Usuário não encontrado.")           
print("Fim do Programa")