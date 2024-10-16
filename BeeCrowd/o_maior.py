numeros = input().split()
a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
maiorAB = int((a + b + abs(a-b))/2)
maiorBC = int((b + c + abs(b-c))/2)
if maiorAB > maiorBC:
    print(f"{maiorAB} eh o maior")
else:
    print(f"{maiorBC} eh o maior")