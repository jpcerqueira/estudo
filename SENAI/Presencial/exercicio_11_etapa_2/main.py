import os
from aviao import Aviao
from companhia import Companhia
from menu import Menu
from cliente import Cliente
from voo import Voo
from reserva import Reserva
from relatorio import Relatorio
from passageiro import Passageiro
from teste import carregar_dados_teste

menu = Menu()
companhia = Companhia()
cliente = Cliente()
voo = Voo()
reserva = Reserva()
relatorio = Relatorio(voo.voos)
passageiro = Passageiro(reserva)

resultado = carregar_dados_teste(companhia, voo, cliente, reserva) # Carregar os dados de teste

def main():
    while True:
        os.system('cls')
        menu.abrir_menu_principal()
        opcao_menu = int(input())

        if opcao_menu == 1:  # Menu Atendente
            while True:
                os.system('cls')
                menu.abrir_menu_atendente()
                opcao_atendente = int(input())
                if opcao_atendente == 1:  # Menu Aviões
                    while True:
                        os.system('cls')
                        menu.abrir_menu_avioes()
                        opcao_avioes = int(input())
                        if opcao_avioes == 1:  # Cadastrar avião
                            identificacao = input('Digite o prefixo do avião: ')
                            total_assentos = int(input('Digite a quantidade de assentos: '))
                            companhia.adicionar_aviao(identificacao, total_assentos)
                            input('Pressione Enter para continuar.')
                        elif opcao_avioes == 2:  # Deletar avião
                            companhia.listar_avioes()
                            nome_aviao = input('Digite o prefixo do avião a ser deletado: ')
                            companhia.deletar_aviao(nome_aviao)
                            input('Pressione Enter para continuar.')
                        elif opcao_avioes == 3:  # Listar aviões
                            companhia.listar_avioes()
                            input('Pressione Enter para continuar.')
                        elif opcao_avioes == 0:  # Retornar ao menu anterior
                            break

                elif opcao_atendente == 2:  # Menu Voos
                    while True:
                        os.system('cls')
                        menu.abrir_menu_voos()
                        opcao_voos = int(input())
                        if opcao_voos == 1:  # Criar voo
                            companhia.listar_avioes()
                            idx_aviao = int(input('Digite o índice do avião para o voo: '))
                            origem = input('Digite a origem do voo: ')
                            destino = input('Digite o destino do voo: ')
                            voo.criar_voo(companhia.avioes[idx_aviao], origem, destino)
                            input('Pressione Enter para continuar.')
                        elif opcao_voos == 2:  # Deletar voo
                            voo.listar_voos()
                            idx_voo = int(input('Digite o índice do voo a ser deletado: '))
                            voo.deletar_voo(idx_voo)
                            input('Pressione Enter para continuar.')
                        elif opcao_voos == 3:  # Listar voos
                            voo.listar_voos()
                            input('Pressione Enter para continuar.')
                        elif opcao_voos == 0:
                            break

                elif opcao_atendente == 3:  # Menu Clientes
                    while True:
                        os.system('cls')
                        menu.abrir_menu_clientes()
                        opcao_clientes = int(input())
                        if opcao_clientes == 1:  # Cadastrar cliente
                            nome_cliente = input('Digite o nome do cliente: ')
                            cliente.adicionar_cliente(nome_cliente)
                            input('Pressione Enter para continuar.')
                        elif opcao_clientes == 2:  # Deletar cliente
                            cliente.listar_clientes()
                            nome_cliente = input('Digite o nome do cliente a ser deletado: ')
                            cliente.deletar_cliente(nome_cliente)
                            input('Pressione Enter para continuar.')
                        elif opcao_clientes == 3:  # Listar clientes
                            cliente.listar_clientes()
                            input('Pressione Enter para continuar.')
                        elif opcao_clientes == 0:
                            break

                elif opcao_atendente == 4:  # Menu Reservas
                    while True:
                        os.system('cls')
                        menu.abrir_menu_reservas()
                        opcao_reservas = int(input())
                        if opcao_reservas == 1:  # Cadastrar reserva
                            voo.listar_voos()
                            idx_voo = int(input('Digite o índice do voo para a reserva: '))
                            if not (0 <= idx_voo < len(voo.voos)):
                                print('Índice de voo inválido. Tente novamente.')
                                input('Pressione Enter para continuar.')
                                continue
                            cliente.listar_clientes()
                            idx_cliente = int(input('Digite o índice do cliente para a reserva: '))
                            if not (0 <= idx_cliente < len(cliente.clientes)):
                                print('Índice de cliente inválido. Tente novamente.')
                                input('Pressione Enter para continuar.')
                                continue
                            reserva.listar_assentos_disponiveis(voo.voos[idx_voo])
                            assento = int(input('Escolha o número do assento disponível: '))
                            reserva.criar_reserva(voo.voos[idx_voo], cliente.clientes[idx_cliente], assento)
                            input('Pressione Enter para continuar.')
                        elif opcao_reservas == 2:  # Deletar reserva
                            reserva.listar_reservas()
                            idx_reserva = int(input('Digite o índice da reserva a ser deletada: '))
                            reserva.deletar_reserva(idx_reserva)
                            input('Pressione Enter para continuar.')
                        elif opcao_reservas == 3:  # Listar reservas
                            reserva.listar_reservas()
                            input('Pressione Enter para continuar.')
                        elif opcao_reservas == 4:  # Localizar reserva
                            nome_cliente = input('Digite o nome do cliente para localizar a reserva: ')
                            reserva.localizar_reserva(nome_cliente)
                            input('Pressione Enter para continuar.')
                        elif opcao_reservas == 0:  # Retornar ao menu anterior
                            break

                elif opcao_atendente == 5:  # Menu Relatórios
                    while True:
                        os.system('cls')
                        menu.abrir_menu_relatorios()
                        opcao_relatorios = int(input())
                        if opcao_relatorios == 1:  # Gerar relatório do voo
                            voo.listar_voos()
                            idx_voo = int(input('Digite o índice do voo para o relatório: '))
                            os.system('cls')
                            relatorio.gerar_relatorio(voo.voos[idx_voo])
                            input('Pressione Enter para continuar.')
                        elif opcao_relatorios == 0:  # Retornar ao menu anterior
                            break

                elif opcao_atendente == 0:  # Retornar ao menu principal
                    break

        elif opcao_menu == 2:  # Menu Passageiro
            while True:
                os.system('cls')
                menu.abrir_menu_passageiros()
                opcao_passageiro = int(input())
                if opcao_passageiro == 1:  # Alterar reserva
                    passageiro.alterar_assento()
                    input('Pressione Enter para continuar.')
                elif opcao_passageiro == 0:  # Retornar ao menu anterior
                    break

        elif opcao_menu == 0:  # Finalizar programa
            os.system('cls')
            break


if __name__ == '__main__':
    main()