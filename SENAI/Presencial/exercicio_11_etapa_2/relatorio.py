class Relatorio:
    def __init__(self, voos):
        self.voos = voos

    def gerar_relatorio(self, voo):
        aviao = voo['aviao']
        ocupacao_atual = (len(voo['reservas']) / aviao.total_assentos) * 100
        print(f'=== Relatório do Voo {voo['numero']} ===\n')
        print(f'====== Info. Avião ======')
        print(f'Avião: {aviao.identificacao}')
        print(f'Ocupação máxima: {aviao.total_assentos}\n')
        print(f'======= Info. Voo =======')
        print(f'Origem: {voo['origem']}')
        print(f'Destino: {voo['destino']}')
        print(f'Quantidade de assentos reservados: {len(voo['reservas'])}')
        print(f'Quantidade de assentos vagos: {aviao.total_assentos - len(voo['reservas'])}')
        print(f'Ocupação atual: {ocupacao_atual:.2f}%\n')
        print(f'====== Passageiros ======')
        for reserva in voo['reservas']:
            print(f'Cliente: {reserva[0].nome}, Assento: {reserva[1]}')
        print()