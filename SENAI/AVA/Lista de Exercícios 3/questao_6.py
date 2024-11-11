#6. Sequência de Fibonacci: - Escreva um programa que use um loop `while` para gerar e imprimir os primeiros `n` números da sequência de Fibonacci, onde `n` é fornecido pelo usuário.

posicao = int(input('Digite um número da posição desejada da sequência de Fibonacci: '))
contador:int = 0
left:int = 0
right:int = 1
resultado:int = 0
print('A sequência socilitada é: ')
print('1')
while posicao - 1 != contador:
    contador += 1
    resultado = left + right
    left = right
    right = resultado
    print(resultado)