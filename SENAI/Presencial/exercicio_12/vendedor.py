from funcionario import Funcionario

class Vendedor(Funcionario):

    def __init__(self, nome, salario_base, bonus, vendas, comissao):
        super().__init__(nome, salario_base, bonus)
        self.vendas = vendas
        self.comissao = comissao

    def calcular_salario(self):
        return super().calcular_salario() + (self.vendas * self.comissao)

    def descrever(self, salario_bonus):
        return super().descrever(salario_bonus)

#teste
def main():
    nome = 'Rita'
    salario_base = 1600
    bonus = 1.10
    vendas = 40000
    comissao = 0.05

    vendedor1 = Vendedor(nome, salario_base, bonus, vendas, comissao)

    salario_final  = Vendedor.calcular_salario(vendedor1)

    print(Vendedor.descrever(vendedor1, salario_final))
    
if __name__ == '__main__':
    main()