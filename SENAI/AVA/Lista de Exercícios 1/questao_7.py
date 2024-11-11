idade = int(input('Digite uma idade: '))

if idade <= 2:
    print('A pessoa é um bebê.')
elif idade >= 3 and idade <= 12:
    print('A pessoa é um criança.')
elif idade >= 13 and idade <= 19:
    print('A pessoa é um adolecente.')
elif idade >= 20 and idade <= 59:
    print('A pessoa é um adulto.')   
else:
    print('A pessoa é um idoso.')