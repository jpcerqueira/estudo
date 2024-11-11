buuble = [7, 5, 10, 6, 8]
tamanho_lista = len(buuble) - 1
#p:int = None
while (tamanho_lista):
    for i in range(0, tamanho_lista):
        if buuble[i] > buuble[i + 1]:
            (buuble[i], buuble[i + 1]) = (buuble[i + 1], buuble[i]) #swap
            # p = buuble[i]
            # buuble[i] = buuble[i + 1]
            # buuble[i + 1] = p
            # p = None
    tamanho_lista -= 1
print(buuble)