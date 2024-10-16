valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
if (a==0):
    print("Impossivel calcular")
    quit()
delta = (b**2 - 4 * a * c)
raizdelta = (delta)**(1/2)

x1 = (-b + raizdelta) / (2 * a)
x2 = (-b - raizdelta) / (2 * a)

# print(delta)
# print(raizdelta)
# print(x1)
# print(x2)
if (delta < 0):
    print("Impossivel calcular")
else:
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")