import os
from cardapio import Cardapio
from pedido import Pedido
from menu import Menu

menu = Menu()
cardapio = Cardapio()
pedido = Pedido()

def main():

    while True:
        os.system('cls')   
        menu.abrir_menu_principal()
        item_menu:int = int(input())

        if item_menu == 1:

            while True:
                os.system('cls')
                menu.abrir_menu_pedido()
                item_menu:int = int(input())

                if item_menu == 1:
                    os.system('cls') 
                    item = input('Digite o nome do item: ')
                    quantidade:int = int(input('Digite a quantidade do item: '))
                    pedido.adicionar_pedido(item, quantidade)

                elif item_menu == 2:
                    os.system('cls')
                    while True:
                        pedido.mostrar_pedidos()
                        menu_voltar:int = int(input('0 - Retornar ao menu anterior\n'))
                        if menu_voltar == 0:
                            break

                elif item_menu == 3:
                    os.system('cls')
                    while True:
                        total = pedido.calcular_total(cardapio)
                        print(f'Total da conta: R$ {total:.2f}')
                        menu_voltar:int = int(input('0 - Retornar ao menu anterior\n'))
                        if menu_voltar == 0:
                            break

                elif item_menu == 0:
                    break

        elif item_menu == 2:

            while True:
                os.system('cls')    
                menu.abrir_menu_cadastro()
                item_menu:int = int(input())
                print()

                if item_menu == 1:
                    os.system('cls') 
                    nome = input('Digite o nome do item: ')
                    valor:float = float(input('Digite o valor do item: '))
                    cardapio.adicionar_item(nome, valor)

                elif item_menu == 2:
                    os.system('cls')
                    nome_a_remover = input('Digite o nome do item a ser removido: ')
                    cardapio.remover_item(nome_a_remover)

                elif item_menu == 3:
                    os.system("cls")
                    while True:
                        cardapio.mostrar_cardapio()
                        menu_voltar = int(input('0 - Retornar ao menu anterior\n'))
                        if menu_voltar == 0:
                            break

                elif item_menu == 0:
                    break

        elif item_menu == 0:
            os.system('cls')
            print('Saindo do programa.')
            break


if __name__ == '__main__':
    main()