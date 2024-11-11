saida = 0
soma = 0
while (saida>=0):
    saida = int(input(f"Insira um número:"))
    if (saida >= 0):
        soma = soma + saida
print(f"A soma dos números: {soma}")