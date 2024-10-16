entrada = input().split()
n1 = float(entrada[0]) * 2
n2 = float(entrada[1]) * 3
n3 = float(entrada[2]) * 4
n4 = float(entrada[3]) * 1
media = (n1 + n2 + n3 + n4)/10
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    n5 = float(input())
    print(f'Nota do exame: {n5:.1f}')
    mediafinal = (media + n5)/2
    if mediafinal >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print(f'Media final: {mediafinal:.1f}')