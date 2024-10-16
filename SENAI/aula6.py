tamanho_maximo:int = 20
pilha = []

def abrirMenu() -> None:
    print("1 - Empilhar")
    print("2 - Desempilhar")
    print("3 - Limpar pilha")
    print("4 - Listar pilha")
    print("5 - Pilha vazia?")
    print("6 - Fechar programa")

def empilhar(nome: str) -> None: #para melhorar a legibilidade do código, anotar o tipo de parâmetro na função
    pilha.append(nome)

def desempilhar() -> None:
    if len(pilha) > 0:
        print(f"Desempilhando {pilha[-1]}\n")
        pilha.pop() #era so colocar pop 0 aqui
    else:
        print("Pilha vazia\n")

def limpar() -> None:
    if len(pilha) > 0:
        while len(pilha) > 0:
            pilha.pop()
            print("Pilha limpa\n")
    else:
        print("Pilha vazia\n")

def listar() -> None:
    if len(pilha) > 0:
        for item in pilha[::-1]:
            print(f"{item}")
    else:
        print("Pilha vazia")
    print() #usei o print vazio para dar o espaço, pois ficaria ruim dar o espaço entre os itens dentro do loop

def conferirPilha() -> None:
    if len(pilha) == 0:
        print("Verdadeiro\n")
    else:
        print("Falso\n")

while True:

    abrirMenu()
    item_menu:int = int(input()) #anotar tipo na variavel
    print()

    if item_menu == 1:
        if len(pilha) < tamanho_maximo:
            nome:str = input("Digite o nome para guardar na pilha: ") #anotar tipo na variavel, o input já retorna um valor como string
            empilhar(nome)
        else:
            print("Pilha cheia\n")
    
    elif item_menu == 2:
        desempilhar()

    elif item_menu == 3:
        limpar()
    
    elif item_menu == 4:
        listar()

    elif item_menu == 5:
        conferirPilha()

    elif item_menu == 6:
        break