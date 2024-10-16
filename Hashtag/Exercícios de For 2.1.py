meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
maior_venda = 0
vendedores_meta = []
for venda in vendas:
    if venda[1] >= meta:
        vendedores_meta.append(venda)
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        nome_venda = venda[0]

porcentagem_meta = len(vendedores_meta) / len(vendas)
print(f"{porcentagem_meta:.1%}")
print(f"O maior vendedor é: {nome_venda}")