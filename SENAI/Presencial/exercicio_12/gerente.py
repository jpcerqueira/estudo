from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base, bonus)

    def calcular_salario(self):
        return super().calcular_salario()
    
    def descrever(self, salario_bonus):
        return super().descrever(salario_bonus)
    
#teste
def main():
    nome = 'Maria'
    salario_base = 3000
    bonus = 1.10

    gerente1 = Gerente(nome, salario_base, bonus)

    salario_bonus = Gerente.calcular_salario(gerente1)

    print(Gerente.descrever(gerente1, salario_bonus))

if __name__ == '__main__':
    main()