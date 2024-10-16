class Usuario:
    def init(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

usuarios = []

def exibirMenu():
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Buscar usuario por Nome")
    print("4 - Sair do sistema")

def cadastrarUsuario():
    nome = input("Informe o nome: ")
    idade = input("Informe a idade: ")
    usuario = Usuario(nome, idade)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listarUsuarios():
    print(" Usuários cadastrados ")
    for usuario in usuarios:
        print(f"Nome: {usuario.nome}, Idade: {usuario.idade}")
    print()

def buscarUsuario(nome):
    for usuario in usuarios:
        if usuario.nome.lower() == nome.lower(): #lower?
            return f"{usuario.nome} está na lista com idade {usuario.idade}."
    return f"{nome} não encontrado." # talvez não precise do return, pq não é necessário a variavel, apenas a informação

quantidade_maxima_usuarios = int(input("Informe a quantidade máxima de usuários que deseja: "))
while True:
    exibirMenu()
    opcao_menu = int(input("Informe a opção desejada: "))

    if opcao_menu == 1:
        if quantidade_maxima_usuarios == len(usuarios):
            print("Atingiu a quantidade máxima de usuários!!!!")
        else:
            cadastrarUsuario()
    elif opcao_menu == 2:
        listarUsuarios()
    elif opcao_menu == 3:
        nome_busca = input("Informe o nome a ser buscado: ")
        print(buscarUsuario(nome_busca))
    elif opcao_menu == 4:
        break
    else:
        print("Opção inválida, tente novamente.")