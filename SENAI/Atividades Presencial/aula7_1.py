def abrir_menu():
    print('1 - Adicionar nome a fila')
    print('2 - Remover nome a fila')
    print('3 - Limpar fila completa')
    print('4 - Listar fila')
    print('5 - Fila está vazia?')
    print('6 - Sair do sistema\n')

def adicionar(item):
    fila.append(item)

def remover():
    fila.pop(0)

def limpar():
    while fila:
        fila.pop()

def listar():
    for i in fila:
        print(i)

def conferir():
    if len(fila) > 0:
        print('Falso\n')
    else:
        print('Verdadeiro\n')

tamanho_fila:int = 25 #define tamanho da fila
fila:str = [] * tamanho_fila

while True:
    
    abrir_menu()

    menu = int(input('Informe o menu a acessar:\n'))

    if menu == 1:
        if len(fila) < tamanho_fila:
            item:str = input('Digite o nome a adicionar na fila: ')
            print()
            adicionar(item)
        else:
            print('Fila cheia!\n')

    if menu == 2:
        if len(fila) > 0:
            remover()
        else:
            print('Fila vazia!\n')

    if menu == 3:
        if len(fila) > 0:   
            limpar()
        else:
            print('Fila vazia!\n')

    if menu == 4:
        if len(fila) > 0:
            listar()
        else:
            print('Fila vazia!\n')

    if menu == 5:
        conferir()

    if menu == 6:
        break

print('Fim do programa!')