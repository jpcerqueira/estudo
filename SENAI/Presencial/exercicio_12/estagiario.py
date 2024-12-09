from funcionario import Funcionario

class Estagiario(Funcionario):

    def __init__(self, nome, salario_base, bonus, horas_trabalhadas, valor_por_hora):
        super().__init__(nome, salario_base, bonus)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcular_salario(self):
        return super().calcular_salario() + (self.horas_trabalhadas * self.valor_por_hora)
    
    def descrever(self, salario_bonus):
        return super().descrever(salario_bonus)

#teste
def main():
    nome = 'Victor'
    salario_base = 500
    bonus = 1.10
    horas_trabalhadas = 120
    valor_por_hora = 5.5

    estagiario1 = Estagiario(nome, salario_base, bonus, horas_trabalhadas, valor_por_hora)

    salario_final  = Estagiario.calcular_salario(estagiario1)

    print(Estagiario.descrever(estagiario1, salario_final))

if __name__ == '__main__':
    main()