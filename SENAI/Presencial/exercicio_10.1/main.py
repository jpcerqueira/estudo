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
                    while True:
                        os.system('cls')
                        item:str = input('Digite o nome do item: ')
                        quantidade:int = int(input('Digite a quantidade do item: '))
                        pedido.adicionar_item(item, quantidade)
                        mais_item:str = input('Deseja adicionar outro item? (s/n)\n')
                        if mais_item == 'n':
                            break
                    pedido.finalizar_pedido()

                elif item_menu == 2:
                    os.system('cls')
                    pedido.mostrar_todos_pedidos()
                    input('Pressione Enter para voltar ao menu anterior\n')

                elif item_menu == 3:
                    os.system('cls')
                    if pedido.pedidos:
                        indice = int(input(f'Selecione o número do pedido (1 a {len(pedido.pedidos)}): ')) - 1
                        total:float = pedido.calcular_total_por_indice(indice, cardapio)
                        print(f'Total do pedido {indice + 1}: R$ {total:.2f}')
                    else:
                        print("Nenhum pedido disponível para calcular.")
                    input('Pressione Enter para voltar ao menu anterior\n')

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
                    nome:str = input('Digite o nome do item: ')
                    valor:float = float(input('Digite o valor do item: '))
                    cardapio.adicionar_item(nome, valor)

                elif item_menu == 2:
                    os.system('cls')
                    nome_a_remover = input('Digite o nome do item a ser removido: ')
                    cardapio.remover_item(nome_a_remover)

                elif item_menu == 3:
                    os.system("cls")
                    cardapio.mostrar_cardapio()
                    input('Pressione Enter para voltar ao menu anterior\n')

                elif item_menu == 0:
                    break

        elif item_menu == 0:
            os.system('cls')
            print('Saindo do programa.')
            break

if __name__ == '__main__':
    main()