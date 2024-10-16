class Usuario:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
usuarios = []

def exibirMenu():
    print("--------------------------")
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Buscar usuario por Nome")
    print("4 - Deletar usuário")
    print("5 - Sair do sistema")
    print("--------------------------")

def cadastrarUsuario():
    nome = input("Infome o nome: ") #instância
    idade = input("Informe a idade: ")
    usuario = Usuario (nome, idade)
    usuarios.append(usuario)               
    print("Usuário cadastrado com sucesso!")

def listarUsuarios():
    print("***** Usuários cadastrados *****")
    for i, usuario in enumerate(usuarios):
        print("Nome: ", usuario.nome) 
        print("Idade: ", usuario.idade)
        print(f"Índice: {i}")

def buscarUsuario(nome):
    encontrado = False
    for i, usuario in enumerate(usuarios):
        if (usuario.nome == nome):
            print(f"Usuário encontrado:  {usuario.nome}")
            print(f"Idade:  {usuario.idade}")
            print(f"Índice: {i}")
            encontrado = True
            break
    if (encontrado == False): # ou 'not encontrado' pois considera só se o encontrado for false 
        print("-----------------------")
        print("Usuário não encontrado.")
        print("-----------------------")

def deletarUsuario(indice):
    usuarios.pop(indice)
    print("Usuário deletado.")




quantidade_maxima_usuarios = int(input("Informe a quantidade máxima de usuários que deseja: "))
while(True):
    exibirMenu()

    opcao_menu = int(input("Informe a opção desejada? "))

    if (opcao_menu == 1):
        if (quantidade_maxima_usuarios == len(usuarios)):
            print("Atingiu a quantidade máxima de usuários!!!!")
        else:
            cadastrarUsuario()
    elif (opcao_menu == 2):
        listarUsuarios()
    elif (opcao_menu == 3):
        localizar = input("Digite o nome do usuário que procura: ")
        buscarUsuario(localizar)
    elif (opcao_menu == 4):
        indice = int(input("Digite o índice do usuário para deletar: "))
        deletarUsuario(indice) #qual a melhor convensão para o argumento/parâmetro?
    elif (opcao_menu == 5):
        break
print("Fim do programa")