class funcionario:
    def __init__(self, nome, salario_b):
        self.nome = nome
        self.salario_b = salario_b

    def calcular_salario(self):
        return self.salario_b

    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"\nSalário: {self.salario_b:.2f}")

class FuncionarioComissionado(funcionario):
    def __init__(self, nome, salario_b, comissao):
        super().__init__(nome, salario_b)   
        self.comissao = comissao 


    def calcular_salario(self):
        return self.salario_b + self.comissao

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Comissão: R$ {self.comissao:.2f}")
        print(f"Salário Total: R$ {self.calcular_salario():.2f}")

def main():
    func1 =  funcionario("Maria", 4444)
    func2 = FuncionarioComissionado("João", 2700, 900)

    func1.exibir_dados()
    print("------------------------------------")
    func2.exibir_dados()
    print()



if __name__ == "__main__":
    main()

    