#dias = int(input())
#ano = dias // 365
#dias = dias % 365
#mes = dias // 30
#dias = dias % 30
#print(f"{ano} ano(s)")
#print(f"{mes} mes(es)")
#print(f"{dias} dia(s)")

dias = int(input())
x = [365, 30, 1]
y = ["ano(s)", "mes(es)", "dia(s)"]
v = -1
for i in x:
    dias_restantes = dias // i
    dias = dias % i
    v = v + 1
    print(f"{dias_restantes} {y[v]}")