quantidadeUsuarios = int(input("Quantos usuários deseja cadastrar? "))
nomes = [""] * quantidadeUsuarios # vetor dinâmico
idades = [0] * quantidadeUsuarios # coloca zero para atribuir um valor inteiro ao vetor
emails = [""] * quantidadeUsuarios
usuarios_cadastrados = 0
i = 0
def exibir_menu():
    print ("\n Menu")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Sair do sistema")
    return int(input("Escolher uma opção: "))
while True:
    opcao = exibir_menu() # atribui a função para uma variável para chamar a função
    if (opcao==1):
        if usuarios_cadastrados < quantidadeUsuarios:
            nome  = input(f"Digite o nome do usuário {usuarios_cadastrados + 1}: ") # não é incremtno, apenas para quando iniciar mostrar o 1
            idade = int(input("Digite a idade do usuário: "))
            email = input("Digite o e-mail do usuário: ")
            nomes[usuarios_cadastrados] = nome #colocando o nome dentro do vetor atraves do incremento para não substituir o anterior
            idades[usuarios_cadastrados] = idade
            emails[usuarios_cadastrados] = email
            usuarios_cadastrados += 1 #incremento
            print(f"Usuário {nome}, {idade}, {email} foram cadastrados co sucesso") # f é uma estrutura para poder dizer que tipo de dado vai aparecer na
    elif (opcao==2):
        if usuarios_cadastrados == 0:
            print("Não há usuários cadastrados")
        else:
            for i in range(usuarios_cadastrados):
                print(f"Nome: {nomes[i]}, Idade: {idades[i]}, E-mail: {emails[i]}")
    elif opcao==3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida e encerra o programa")