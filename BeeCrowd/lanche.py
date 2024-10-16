entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
menu = (0, 4, 4.5, 5, 2, 1.5)
total = menu[a] * b
print(f'Total: R$ {total:.2f}')