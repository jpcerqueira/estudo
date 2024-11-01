numero = input('Digite seguidamente 3 números inteiros: ').split()
numero1 = int(numero[0])
numero2 = int(numero[1])
numero3 = int(numero[2])

if numero1 < numero2 and numero1 < numero3:
    print(f'O menor número é o {numero1}.')
elif numero2 < numero1 and numero2 < numero3:
    print(f'O menor número é o {numero2}.')
else:
    print(f'O menor número é o {numero3}.')