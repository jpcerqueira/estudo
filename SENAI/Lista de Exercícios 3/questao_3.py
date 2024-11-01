# 3. Entrada de dados até o zero: - Escreva um programa que peça ao usuário para digitar números até que ele digite zero. Use um loop `do-while`.
numero:int = 1
while numero != 0:
    numero = int(input('Digite um número para aparecer na tela, se quiser encerrar digite 0: '))
    print(f'O número digitado foi: {numero}')
print('Fim do programa.')