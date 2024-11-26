class Menu:
    def abrir_menu_principal(self):
        print("=== Menu Principal ===")
        print("1. Atendente")
        print("2. Passageiro")
        print("0. Sair")
        print("Escolha uma opção:")

    def abrir_menu_atendente(self):
        print("=== Menu Atendente ===")
        print("1. Aviões")
        print("2. Voos")
        print("3. Clientes")
        print("4. Reservas")
        print("5. Relatórios")
        print("0. Voltar ao menu principal")
        print("Escolha uma opção:")

    def abrir_menu_avioes(self):
        print("=== Menu Aviões ===")
        print("1. Cadastrar avião")
        print("2. Deletar avião")
        print("3. Listar aviões")
        print("0. Voltar ao menu anterior")
        print("Escolha uma opção:")

    def abrir_menu_voos(self):
        print("=== Menu Voos ===")
        print("1. Criar voo")
        print("2. Deletar voo")
        print("3. Listar voos")
        print("0. Voltar ao menu anterior")
        print("Escolha uma opção:")

    def abrir_menu_clientes(self):
        print("=== Menu Clientes ===")
        print("1. Cadastrar cliente")
        print("2. Deletar cliente")
        print("3. Listar clientes")
        print("0. Voltar ao menu anterior")
        print("Escolha uma opção:")

    def abrir_menu_reservas(self):
        print("=== Menu Reservas ===")
        print("1. Cadastrar reserva")
        print("2. Deletar reserva")
        print("3. Listar reservas")
        print("4. Localizar reserva")
        print("0. Voltar ao menu anterior")
        print("Escolha uma opção:")

    def abrir_menu_relatorios(self):
        print("=== Menu Relatórios ===")
        print("1. Gerar relatório de voo")
        print("0. Voltar ao menu anterior")
        print("Escolha uma opção:")

    def abrir_menu_passageiros(self):
        print("=== Menu Passageiro ===")
        print("1 - Localizar reserva")
        print("2 - Alterar reserva")
        print("0 - Voltar ao menu anterior")