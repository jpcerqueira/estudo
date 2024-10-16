#colocar uma função? com uma condição para ver se foi lido um dado de entrada, caso não seja, mostrar na tela que não foi digitado um valor
#ex: if 'variavel': -> se a variavel estiver preenchida faça
#ou if 'variavel' == '' ou 0: -> se a variavel não tiver preenchida, só com a entrada vazia que fica as aspas ou 0, faça ## mas tomar cuidado pois o numero de entrada pode ser realmente zero

qtd = int(input("Quantos usuários serão cadastrados?"))
menu = 0
usuarios = []
while (menu != 3):
    print("-----------------------------")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Sair do Sistema")
    print("-----------------------------")
    menu = int(input())
    if (menu == 1):
        if (len(usuarios) < qtd):                   # condição atraves pela quantidade de itens na lista por quantidade definida pelo usuário no início do programa
            usuario = input("Nome do usuário:")     # atribuição a variavel usuario
            usuarios.append(usuario)                # adiciona a variavel usuario ao vetor usuarios atraves do metodo append
        else:
            print("Número de cadastros completo.")
    if (menu == 2):
        if (len(usuarios) == 0):
            print("Nenhum usuário cadastrado.")
        else:
            print(usuarios)
print("Fim do Programa")