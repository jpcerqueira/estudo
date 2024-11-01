# 4. Fatorial de um número: - Escreva um programa que calcule o fatorial de um número dado pelo usuário usando um loop `while`.

numero = int(input('Digite um número para saber seu fatorial: '))
fatorial:int = numero
start = numero
if numero == 0:
    print(f'O fatorial de "{start}" é : 1')
elif numero == 1:
    print(f'O fatorial de "{start}" é : 1')
else:
    while numero:
        fatorial = fatorial * (numero - 1)
        numero -= 1
        if numero == 1:
            break
    print(f'O fatorial de "{start}" é : {fatorial}')