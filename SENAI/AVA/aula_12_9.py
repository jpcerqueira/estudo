#Função para mostrar o menu ao usuário
def mostrar_menu (): #def = função, nome da função, () local para o parametro
    print("Menu de Opções:")
    print(f"1 - Cadastrar novo usuário: ")
    print(f"2 - Listar todos os usuários cadastrados: ")
    print(f"3 - Sair")

#Função para cadastro dos usuários
def cadastrar_usuario(usuarios): #dois pontos é tudo que ta para baixo
    nome = input("Digite o nome do usuário: ") #declarando uma variável para receber o nome
    idade = input("Digite a idade do usuário: ") #declarando uma variável para receber o nome
    email = input("Digite seu e-mail: ") #declarando uma variável para receber o e-mail

    usuario = {"nome": nome, "idade": idade, "email": email} #vetor com os dados do usuário, uma especie de dicionário
    usuarios.append(usuario) #o ponto é um appede, que insere um novo elemento ao fim da lista, parecido com uma matriz  // adicionando o usuario cadastrado no fim de uma
    print("Usuário cadastrado com sucesso") # mostrar na tela mensagem de concluido

#Função para listar os usuários na tela
def listar_usuarios(usuarios):
    if len(usuarios) == 0: #len conta itens da lista - : é o faça   #Lógica SE
        print("Nenhum usuário cadastrado")                          #mostra na tela
    else:                                                           #senao
        print("Lista dos usuários cadastrados")
        #ESTRUTURA DE REPETIÇÃO
        for i, usuarios in enumerate(usuarios, start=1): # i de inteiro #enumerante retorna a quantidade de dados de um vetor em uma lista
            print(f"Usuário: {i}") #mostrar na tela a posição de cadastro
            print(f"Nome: {usuarios['nome']}")
            print(f"Idade: {usuarios['idade']}")
            print(f"E-mail: {usuarios['email']}")                                                                   