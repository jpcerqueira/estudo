n = float(input())
nota100 = int(n / 100) # o quociente da divisão é/são a quantidade de notas
n_restantes = n % 100 # o resto da divisão são as notas de 1
nota50 = int(n_restantes / 50)
n_restantes = n_restantes % 50
nota20 = int(n_restantes / 20)
n_restantes = n_restantes % 20
nota10 = int(n_restantes / 10)
n_restantes = n_restantes % 10
nota5 = int(n_restantes / 5)
n_restantes = n_restantes % 5
nota2 = int(n_restantes / 2)
n_restantes = n_restantes % 2
moeda1 = int(n_restantes / 1)
n_restantes = n_restantes % 1
moeda050 = int(n_restantes / 0.5)
n_restantes = n_restantes % 0.5
moeda025 = int(n_restantes / 0.25)
n_restantes = n_restantes % 0.25
moeda010 = int(n_restantes / 0.10)
n_restantes = n_restantes % 0.10
moeda005 = int(n_restantes / 0.05)
n_restantes = n_restantes % 0.05
moeda001 = int(round(n_restantes,2) / 0.01)
n_restantes = n_restantes % 0.01
print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda1} moeda(s) de R$ 1.00")
print(f"{moeda050} moeda(s) de R$ 0.50")
print(f"{moeda025} moeda(s) de R$ 0.25")
print(f"{moeda010} moeda(s) de R$ 0.10")
print(f"{moeda005} moeda(s) de R$ 0.05")
print(f"{moeda001} moeda(s) de R$ 0.01")