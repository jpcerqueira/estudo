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

    def gerar_ranking_voos(self):
        ocupacoes = []
        for voo in self.voos:
            total_assentos = voo['aviao'].total_assentos
            assentos_ocupados = len(voo['reservas'])
            ocupacao_percentual = (assentos_ocupados / total_assentos) * 100
            ocupacoes.append((voo, ocupacao_percentual))
        
        for i in range(len(ocupacoes)):
            for j in range(i + 1, len(ocupacoes)):
                if ocupacoes[i][1] < ocupacoes[j][1]:
                    ocupacoes[i], ocupacoes[j] = ocupacoes[j], ocupacoes[i]

        print("=== Ranking de Voos Mais Ocupados ===")
        for idx, (voo, ocupacao) in enumerate(ocupacoes, start=1):
            print(f"{idx}. Voo {voo['numero']} - {voo['origem']} para {voo['destino']} - Ocupação: {ocupacao:.2f}%")