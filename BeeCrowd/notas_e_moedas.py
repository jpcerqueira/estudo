moeda_troco = float(input())
lista_moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
valor = 0
for moeda in lista_moedas:
    valor = round(moeda_troco,2) // moeda
#    if moeda_troco > 0 and moeda_troco < 0.01:
#        valor += 1
    moeda_troco -= valor*moeda
    #moeda_troco = moeda_troco % moeda
    if moeda == 100:
        print ("NOTAS:")
    elif moeda == 1:
        print ("MOEDAS:")
    elif moeda > 1:
        print(f"{int(valor)} nota(s) de R$ {moeda:.2f}")
    else:
        print(f"{int(valor)} moeda(s) de R$ {moeda:.2f}")
#if moeda_troco < 0.01 and moeda_troco > 0:
#        valor += 1
#        print(f"{int(valor)} moeda(s) de R$ {moeda:.2f}")