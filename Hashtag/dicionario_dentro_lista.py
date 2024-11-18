pedidos = []  # Lista para armazenar todos os pedidos

while True:
    pedido_atual = {'Item': [], 'Valor': []}  # Novo pedido como um dicionário
    while True:
        item = input('Digite o nome do item (ou "sair" para finalizar o pedido): ')
        if item.lower() == 'sair':
            break
        preco = float(input('Digite o preço: '))

        # Adiciona o item e o preço ao pedido atual
        pedido_atual['Item'].append(item)
        pedido_atual['Valor'].append(preco)
    
    pedidos.append(pedido_atual)  # Adiciona o pedido atual à lista de pedidos
    
    fechar = int(input('Deseja fazer outro pedido? Digite 0 para sair ou 1 para continuar: '))
    if fechar == 0:
        break

print(pedidos)  # Exibe todos os pedidos

# Exemplo de acesso: soma do preço do segundo item do primeiro pedido
if len(pedidos) > 0 and len(pedidos[0]['Valor']) > 1:
    soma = pedidos[0]['Valor'][1] + 2
    print(f'Soma do segundo item do primeiro pedido com 2: {soma}')
