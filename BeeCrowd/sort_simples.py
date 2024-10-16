entrada = input().split()
#entrada2 = entrada.copy()
entrada2 = ['0','0','0']
for i, x in enumerate(entrada):
    entrada2[i] = x
for i in range(len(entrada)):
    entrada[i] = int(entrada[i])
repeticao = len(entrada) - 1
while(repeticao):
    for i in range(repeticao):
        if entrada[i] > entrada[i + 1]:
            entrada[i], entrada[i + 1] = entrada[i + 1], entrada[i]
    repeticao -= 1
for i in entrada:
    print(i)
print()
for i in entrada2:
    print(i)