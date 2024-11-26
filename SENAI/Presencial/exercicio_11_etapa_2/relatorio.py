class Relatorio:
    def __init__(self, voos):
        self.voos = voos

    def gerar_relatorio(self, voo):
        print(f"=== Relatório do Voo {voo['numero']} ===")
        print(f"Origem: {voo['origem']}")
        print(f"Destino: {voo['destino']}")
        print(f"Quantidade de reservas: {len(voo['reservas'])}")
        for reserva in voo['reservas']:
            print(f"Cliente: {reserva[0].nome}, Assento: {reserva[1]}")
        input("Pressione Enter para continuar.")