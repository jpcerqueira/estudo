class Reserva:
    def __init__(self):
        self.reservas = []

    def listar_assentos_disponiveis(self, voo):
        assentos_reservados = []
        for reserva in self.reservas:
            if reserva['voo'] == voo:
                assentos_reservados.append(reserva['assento'])
        assentos_totais = list(range(1, voo['aviao'].total_assentos + 1))
        assentos_disponiveis = [assento for assento in assentos_totais if assento not in assentos_reservados]
        print(f'Assentos disponíveis: {', '.join(map(str, assentos_disponiveis))}')
        return assentos_disponiveis

    def criar_reserva(self, voo, cliente, assento):
        assentos_disponiveis = self.listar_assentos_disponiveis(voo)
        if assento in assentos_disponiveis:
            voo['reservas'].append((cliente, assento))
            self.reservas.append({'cliente': cliente, 'voo': voo, 'assento': assento})
            print(f'Reserva feita com sucesso para o cliente {cliente.nome} no assento {assento}.')
        else:
            print('Assento inválido ou já reservado.')

    def deletar_reserva(self, idx_reserva):
        if 0 <= idx_reserva < len(self.reservas):
            self.reservas.pop(idx_reserva)
            print('Reserva deletada com sucesso.')
        else:
            print('Reserva não encontrada.')
    def listar_reservas(self):
        if not self.reservas:
            print('Nenhuma reserva encontrada.')
        else:
            for i, reserva in enumerate(self.reservas):
                print(f'{i} - Cliente: {reserva['cliente'].nome}, Voo {reserva['voo']['numero']}, Assento: {reserva['assento']}')

    def localizar_reserva(self, nome_cliente):
        reservas_encontradas = []
        for reserva in self.reservas:
            if reserva['cliente'].nome.lower() == nome_cliente.lower():
                reservas_encontradas.append(reserva)
        if reservas_encontradas:
            for reserva in reservas_encontradas:
                print(f'Reserva encontrada: Cliente: {reserva['cliente'].nome}, Voo: {reserva['voo']['numero']}, Assento: {reserva['assento']}')
        else:
            print(f'Nenhuma reserva encontrada para o cliente {nome_cliente}.')