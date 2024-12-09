from gerente import Gerente
from vendedor import Vendedor
from estagiario import Estagiario

def main():
    bonus_por_meta:float = 1.10
    salario_gerente:float = 3400
    salario_vendedor:float = 1800
    salario_estagiario:float = 700
    comissao:float = 0.05
    valor_por_hora:float = 6

    gerente1 = Gerente('Paula', salario_gerente, bonus_por_meta)
    vendedor1 = Vendedor('André', salario_vendedor, bonus_por_meta, 40000, comissao)
    vendedor2 = Vendedor('Ana', salario_vendedor, bonus_por_meta, 35000, comissao)
    estagiario1 = Estagiario('Carlos', salario_estagiario, bonus_por_meta, 120, valor_por_hora)

    salario_bonus_gerente = Gerente.calcular_salario(gerente1)
    salario_bonus_vendedor1  = Vendedor.calcular_salario(vendedor1)
    salario_bonus_vendedor2  = Vendedor.calcular_salario(vendedor2)
    salario_bonus_estagiario1  = Estagiario.calcular_salario(estagiario1)

    print(Gerente.descrever(gerente1, salario_bonus_gerente))
    print(Vendedor.descrever(vendedor1, salario_bonus_vendedor1))
    print(Vendedor.descrever(vendedor2, salario_bonus_vendedor2))
    print(Estagiario.descrever(estagiario1, salario_bonus_estagiario1))

if __name__ == '__main__':
    main()