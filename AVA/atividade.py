Realizar a função listar()




tamanho_max = 20 #Definir o tamanho da pilha para 20 posições
pilha = []*tamanho_max #Inicialização da pilha
topo = -1 #Indicador do tpo da pilha, inicia vazio

def vazia():
    if topo == -1:
        return True
    else:
        return False


def empilhar(nome):
    global topo #Modifica a variável topo definida fora da função

    if topo<tamanho_max:
        topo +=1            #soma uma posição na viável auxiliar topo
        pilha[topo] = nome
        print(f"{nome} foi cadastrdo com sucesso")
    else:
        print("Erro ao cadastrar a lista")

def desempilhar():
    global topo
    if not vazia():
        nome = pilha[topo]
        pilha[topo]=""              #Removendo a variável do topo
        topo -= 1
        print("Foi removido")
    else:
        print("Erro: a pilha esta vazia")

#LISTAR OS ELEMENTOS: É IGUAL A IDEIA DE LISTAR O VETOR
def listar():
    for item in pilha[::-1]:
        print(item)
   
def  limpar():
    if not vazio():
        print("Elementos na pilha (no topo da base): ")
        for i in range(topo,-1,1):
            print(pilha[i])
    else
        print("A pilha está vazia ")

while True:
    print("\n Escolha uma opção")
    print("1 - Empilhar a lista")
    print("2 - Desempilhar a lista")
    print("3 - Listar os elementos da lista")
    print("4 - Limpar a lista")
    print("5 - Sair")

    opcao = int(input("Digite sua opção"))
   
    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        empilhar(nome)
   
    elif opcao == 2:
        desempilhar()
   
    elif opcao == 3:
        listar()
   
    elif opcao == 4:
        limpar()

    elif opcao == 5:    
        print("Saindo do programa. Até logo!")  
        break

    else:
        print("Opção inválida!")