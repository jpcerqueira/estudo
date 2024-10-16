plano1 = input().split()
x1 = float(plano1[0])
y1 = float(plano1[1])
plano2 = input().split()
x2 = float(plano2[0])
y2 = float(plano2[1])
distancia = ((x2 - x1)**2 + (y2 - y1)**2 ) **0.5
print(f"{distancia:.4f}")