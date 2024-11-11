# 6) Escreva um programa que use um loop for para calcular a soma dos números de 1 a 100.
soma:int = 0
for i in range(1,101):
    soma += i # soma = soma + i
print (f'O total da soma dos números de 1 a 100 é: {soma}')