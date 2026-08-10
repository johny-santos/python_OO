class Funcionario:
    def __init__(self, nome_funcionario, salario_funcionario):
        self.nome_funcionario = nome_funcionario
        self.salario_funcionario = salario_funcionario

class Departamento:
    def __init__(self, nome_departamento):
        self.nome_departamento = nome_departamento
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário encontrado neste departamento")
        else:
            for f in self.funcionarios:
                print(f"{f.nome_funcionario} - R$ {f.salario_funcionario}")
            print()

    def media_salarial(self):
        if not self.funcionarios:
            return 0

        soma = 0 
        for f in self.funcionarios:
            soma += f.salario

        return soma / len(self.funcionarios)
              

def main():
    funcionarios = []
    departamentos = []

    while True:
        print("\n=================MENU===================\n")
        print("1 - Criar funcionário")
        print("2 - criar Departamento")
        print("3 - Adicionar um funcionário ao Departamento")
        print("4 - listar Funcionários de um Departamento")
        print("5 - Mostrar a média salarial do departamento")
        print("6 - Sair")
        
        opcao = input("\nEscolha uma opção (1-6): ")
        
        if opcao == "1":
            nome_funcionario = input("Digite o nome do funcionário: ")
            salario = float(input("Digite o valor do salário: "))

            
            funcionario = Funcionario(nome_funcionario, salario)

            funcionarios.append(funcionario)

            print("Funcionário criado com Sucesso!")
            
        elif opcao == "2":
            nome_dept = input("Digite o nome do Departamento: ")
            
            
            dept = Departamento(nome_dept)

            departamentos.append(dept)

            print("Departamento criado com Sucesso!")
            
        elif opcao == "3":
            if funcionarios and departamentos:
                print("\nFuncionários: ")
                for i, f in enumerate(funcionarios):
                    print(f"{i + 1}. {f.nome_funcionario}")
                i_funcionario =  int(input("Escolha o número do funcionário")) - 1

                print("\nDepartamentos: ")
                for i, d in enumerate(departamentos):
                    print(f"{i + 1}. {d.nome_departamento}")
                i_dept =  int(input("Escolha o número do departamento")) - 1

                departamentos[i_dept].adicionar_funcionario(funcionarios[i_funcionario])

                print(f"\nFuncionário adicionado ao departamento com sucesso!\n")

            else:
                print("\nCrie funcionários e departamentos primeiro!\n")
                
        elif opcao == "4":
            print("\nDepartamentos: ")
            for i, d in enumerate(departamentos):
                print(f"{i + 1}. {d.nome_departamento}")
            i_dept =  int(input("Escolha o número do departamento")) - 1

            departamentos[i_dept].listar_funcionarios()
        elif opcao == "5":
            print("\nDepartamentos: ")
            for i, d in enumerate(departamentos):
                print(f"{i + 1}. {d.nome_departamento}")
            i_dept =  int(input("Escolha o número do departamento")) - 1

            media = departamentos[i_dept].media_salarial()

            print(f"\nA média salarial: R$ {media:.2f}\n")

        elif opcao == "6":
            print("Saindo...")
            break
           
        else:
            print("Opção inválida, tente novamente")

if __name__ == "__main__":
    main()


