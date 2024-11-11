class Usuario:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

usuarios = []

def exibirMenu():
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Buscar usuario por Nome")
    print("4 - Sair do sistema")

def cadastrarUsuario():
    nome = input("Infome o nome: ")
    idade = input("Infome o idade: ")
    #print()
    greg = Usuario (nome, idade) #instância / criado o objeto
    usuarios.append(greg)
    print("Usuário cadastrado com sucesso!\n")

def listarUsuarios():
    print("Usuários cadastrados")
    for usuario in usuarios:
        print("Nome: ", usuario.nome)
        print("Idade:", usuario.idade)

    print()

def buscarUsuario(nome):
    for usuario in usuarios:
        if (usuario.nome == nome):
            print("Usuário identificado: ", usuario.nome)
            return
        print("Usuário não encontrado")
        print()

quantidade_maxima_usuarios = int(input("Informe a quantidade máxima de usuários que deseja: "))
while(True):
    exibirMenu()

    opcao_menu = int(input("Informe a opção desejada? \n"))
    print()

    if (opcao_menu == 1):
        if (quantidade_maxima_usuarios == len(usuarios)):
            print("Atingiu a quantidade máxima de usuários!!!!\n")
        else:
            cadastrarUsuario()
    if (opcao_menu == 2):
        listarUsuarios()
    if (opcao_menu == 3):
        buscarUsuario(input("Qual nome deseja buscar? \n"))
    if (opcao_menu == 4):
        break