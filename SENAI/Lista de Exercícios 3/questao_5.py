#5. Média de números: - Escreva um programa que use um loop `do-while` para ler números inteiros do usuário até que ele digite um número negativo, e então calcule e imprima a média desses números.
numero:int = 0
soma:int = 0
media:int = 0
contador:int = 0
while numero > -1:
    numero = int(input('Digite um número: '))
    if numero >= 0:
        contador += 1
        soma = numero + soma
        media = soma / contador
print(f'A média dos números digitados é: {media}')