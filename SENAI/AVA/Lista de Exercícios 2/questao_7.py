#7) Escreva um programa que calcule o fatorial de um número inteiro dado pelo usuário usando um loop for.

#5! 5*4*3*2*1

numero = int(input('Digite um número inteiro: '))
multiplicacao:int = numero
for i in range(numero-1,0,-1):
    multiplicacao = i * multiplicacao
    
print(f'O fatorial de {numero} é : {multiplicacao}')