entrada = input().split()
p1 = float(entrada[0])
p2 = float(entrada[1])
if p1 > 0 and p2 > 0:
    print('Q1')
elif p1 < 0 and p2 > 0:
    print('Q2')
elif p1 < 0 and p2 < 0:
    print('Q3')
elif p1 > 0 and p2 < 0:
    print('Q4')
elif p1 == 0 and p2 == 0:
    print('Origem')
elif p1 == 0 and p2 != 0:
    print('Eixo Y')
elif p1 != 0 and p2 == 0:
    print('Eixo X')