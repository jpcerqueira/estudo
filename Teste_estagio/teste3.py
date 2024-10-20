#3) Observe o trecho de código abaixo: 
#int INDICE = 12, 
#SOMA = 0, 
#K = 1; 
#enquanto K < INDICE faça 
#{ K = K + 1; SOMA = SOMA + K; } 
#imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

indice:int = 12
soma:int = 0
k:int = 1

while k < indice:
    k += 1
    soma = soma + k

print(f'O valor da soma é: {soma}')


#resposta = 77