#ITERATIVO

# def fatorial(numero: int):
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado *= i
#     return resultado

# x: int = 3
# print(fatorial(x))


def fatorial (numero:int):
    if numero == 0 or numero == 1:
        return 1
    return numero * fatorial(numero -1) #aqui que chama a função fatorial(4),(3),(2) e finalmente o que fecha (1)

x: int = 5
print(fatorial(x))