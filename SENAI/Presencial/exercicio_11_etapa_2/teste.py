def carregar_dados_teste(companhia, voo, cliente, reserva):

    identificacao_teste = 'PTH-2546'
    total_assentos_teste = 3
    origem_teste = 'FSA'
    destino_teste = 'GRU'
    nome_cliente_teste = 'João Pedro'
    assento_teste = 1


    companhia.adicionar_aviao(identificacao_teste, total_assentos_teste)
    idx_aviao_teste = 0

    voo.criar_voo(companhia.avioes[idx_aviao_teste], origem_teste, destino_teste)
    idx_voo_teste = 0 

    cliente.adicionar_cliente(nome_cliente_teste)
    idx_cliente_teste = 0

    reserva.criar_reserva(voo.voos[idx_voo_teste], cliente.clientes[idx_cliente_teste], assento_teste)
