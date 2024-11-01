#7. Números primos: - Escreva um programa que encontre todos os números primos entre 1 e 100 usando um loop `while`.

print("Números primos entre 1 e 100:")
print(2)
print(3)

numero = 4
while numero <= 100:
    eh_primo = True
    divisor = 2
    while divisor <= numero ** 0.5:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1
    
    if eh_primo:
        print(numero)
    
    numero += 1