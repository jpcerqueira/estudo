# 2. Somatório de números de 1 a 100: - Escreva um programa que use um loop `while` para calcular a soma dos números de 1 a 100.

numero:int = 1
soma:int = 0
while soma != 5050:
    print(f'{numero} + {soma}')
    soma = numero + soma
    numero += 1
    print(f'{soma}')
print(soma)