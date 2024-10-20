#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

entrada:str = input('Digite uma palavra ou frase: ')
qtd_a:int = 0
for i in entrada:
    if i == 'a' or i == 'A':
        qtd_a += 1
if qtd_a > 0:         
    print(f'A palavra ou frase escrita possui a letra "a" e aparece {qtd_a} veze(s)!')
else:
    print('Essa palavra ou frase não possui a letra "a"!')