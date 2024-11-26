import os
from aviao import Aviao
from companhia import Companhia
from menu import Menu

menu = Menu()
aviao = Aviao()
companhia = Companhia()

def main():
    while True:
        os.system('cls')
        menu.abrir_menu_principal()
        nagevacao_menu:int = int(input())

        if nagevacao_menu == 1:
            os.system('cls')
            qtd_avioes:int = int(input('Digite a quantidade de aviões: '))

            for i in range(qtd_avioes):
                identificacao:str = input(f'Digite o prefixo do avião {i + 1}: ')
                total_assentos:int = int(input(f'Digite a quantidade de assentos do avião {i + 1}: '))
                companhia.adicionar_aviao(identificacao, total_assentos)

        elif nagevacao_menu == 2:
            os.system('cls')
            companhia.listar_avioes()
            print()
            input('Pressione Enter para retornar.')

        
        elif nagevacao_menu == 0:
            os.system('cls')
            break

if __name__ == '__main__':
    main()