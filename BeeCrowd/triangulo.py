entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])
if (a + b > c) and (a + c > b) and (b + c > a):
    perimetro_triangulo = a + b + c
    print(f'Perimetro = {perimetro_triangulo:.1f}')
else:
    area_trapezio = ((a + b)*c)/2
    print(f'Area = {area_trapezio:.1f}')