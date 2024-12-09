from abc import ABC

class Funcionario(ABC):

    def __init__(self, nome:str, salario_base:float, bonus:float):
        self.nome = nome
        self.salario_base = salario_base
        self.bonus = bonus
    
    def calcular_salario (self):
        salario_bonus = self.salario_base * self.bonus
        return salario_bonus

    def descrever(self, salario_bonus):
        return f'O colaborador(a) {self.nome} tem um salário base de R$ {self.salario_base:.2f} e um salário com bônus de R$ {salario_bonus:.2f}.'

#teste
def main():
    nome = 'Pedro'
    salario_base = 1200
    bonus = 1.10

    funcionario1 = Funcionario(nome, salario_base, bonus)

    salario_bonus = Funcionario.calcular_salario(funcionario1)

    print(Funcionario.descrever(funcionario1, salario_bonus))

if __name__ == '__main__':
    main()