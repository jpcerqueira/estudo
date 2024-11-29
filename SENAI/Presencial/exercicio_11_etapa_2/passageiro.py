class Passageiro:
    def __init__(self, reserva):
        self.reserva = reserva

    def alterar_assento(self):
        nome_cliente = input("Digite o nome do cliente para localizar a reserva: ")
        reservas_encontradas = [
            (idx, reserva) for idx, reserva in enumerate(self.reserva.reservas) 
            if reserva['cliente'].nome.lower() == nome_cliente.lower()
        ]

        if not reservas_encontradas:
            print("Nenhuma reserva encontrada para o nome fornecido.")
            return

        print("Reservas encontradas:")
        for idx, reserva in reservas_encontradas:
            print(f"Índice: {idx} - Cliente: {reserva['cliente'].nome}, Voo: {reserva['voo']['numero']}, Assento: {reserva['assento']}")

        idx_reserva = int(input("Digite o índice da reserva que deseja alterar: "))
        if idx_reserva not in [idx for idx, _ in reservas_encontradas]:
            print("Índice inválido. Operação cancelada.")
            return

        reserva_selecionada = self.reserva.reservas[idx_reserva]

        assentos_ocupados = [res['assento'] for res in self.reserva.reservas if res['voo'] == reserva_selecionada['voo']]
        total_assentos = reserva_selecionada['voo']['aviao'].total_assentos
        assentos_disponiveis = [i for i in range(1, total_assentos + 1) if i not in assentos_ocupados]

        print("Assentos disponíveis:", assentos_disponiveis)
        novo_assento = int(input("Digite o número do novo assento: "))

        if novo_assento not in assentos_disponiveis:
            print("Assento inválido ou já ocupado. Operação cancelada.")
            return

        self.reserva.deletar_reserva(idx_reserva)
        self.reserva.criar_reserva(reserva_selecionada['voo'], reserva_selecionada['cliente'], novo_assento)