class Reserva:
    def __init__(self):
        self.reservas = []

    def criar_reserva(self, voo, cliente, assento):
        if assento <= voo['aviao'].total_assentos:
            voo['reservas'].append((cliente, assento))
            self.reservas.append({"cliente": cliente, "voo": voo, "assento": assento})
            print(f"Reserva feita com sucesso para o cliente {cliente.nome} no assento {assento}.")
        else:
            print("Assento inválido.")

    def deletar_reserva(self, idx_reserva):
        if 0 <= idx_reserva < len(self.reservas):
            self.reservas.pop(idx_reserva)
            print("Reserva deletada com sucesso.")
        else:
            print("Reserva não encontrada.")

    def listar_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva encontrada.")
        for i, reserva in enumerate(self.reservas):
            print(f"{i} - Cliente: {reserva['cliente'].nome}, Voo {reserva['voo']['numero']}, Assento: {reserva['assento']}")

    def localizar_reserva(self, nome_cliente):
        reservas_encontradas = [reserva for reserva in self.reservas if reserva['cliente'].nome.lower() == nome_cliente.lower()]
        if reservas_encontradas:
            for reserva in reservas_encontradas:
                print(f"Reserva encontrada: Cliente: {reserva['cliente'].nome}, Voo: {reserva['voo']['numero']}, Assento: {reserva['assento']}")
        else:
            print(f"Nenhuma reserva encontrada para o cliente {nome_cliente}.")