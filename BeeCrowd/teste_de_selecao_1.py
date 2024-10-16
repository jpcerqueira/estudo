letras = input().split()
A = int(letras[0])
B = int(letras[1])
C = int(letras[2])
D = int(letras[3])
if (B > C) and (D > A) and ((C + D) > (A + B)) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")