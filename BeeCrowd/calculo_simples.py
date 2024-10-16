entrada1 = input().split() #o split cria uma lista, com vetor inicial [0], e é separado por espaços, onde o parenteses vazio cria essa condição
peca1 = int(entrada1[0]) #o entrada1[0] é a indicação que o valor do vetor recebido primeiro vai ser destinado a essa variavel
qtd_peca1 = int(entrada1[1])
valor_unitario1 = float(entrada1[2])
entrada2 = input().split()
peca2 = int(entrada2[0])
qtd_peca2 = int(entrada2[1])
valor_unitario2 = float(entrada2[2])
total1 = qtd_peca1 * valor_unitario1
total2 = qtd_peca2 * valor_unitario2
total = total1 + total2
print(f"VALOR A PAGAR: R$ {total:.2f}")