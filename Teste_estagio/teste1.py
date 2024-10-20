#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)
#Escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



inicial_1:int = 0
inicial_2:int = 1
numero = int(input("Informe um número: "))

if numero == inicial_1 or numero == inicial_2:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    while inicial_2 < numero:
        p:int = inicial_2
        inicial_2 = inicial_1 + inicial_2
        inicial_1 = p
        p = None
    
    if inicial_2 == numero:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")