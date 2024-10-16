hora = 0
minuto = 0
n = int(input())
while (n != 0):
    if (n >= 3600):
        n = n - 3600
        hora = hora + 1
    elif (n >= 60):
        n = n - 60
        minuto = minuto + 1
    else:
        segundo = n
        n = n - n
print(f"{hora}:{minuto}:{segundo}")