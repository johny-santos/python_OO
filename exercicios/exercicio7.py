class Casa:
    class __comodo:
        def __init__(self, nome, area):
            self.__nome = nome
            self.__area = area

        def get_nome(self):
            return self.__nome

        def get_area(self):
            return self.__area

        def set_nome(self, nome):
            self.__nome = nome 

        def set_area(self, area):
            if area > 0:
                self.__area = area
            else:
                print("A área deve ser um número positivo!")

    def __init__(self):
        self.__comodos = [] 

    def adicionar_comodo(self, nome, area):
        novo_comodo = self.__comodo(nome, area)

        self.__comodos.append(novo_comodo)
        print(f"O cômodo: '{nome}', foi adicionado com sucesso!")

    def listar_comodos(self):
        if not self.__comodos:
            print("\nNenhum cômodo encontrado, acrescente um para vê-los aqui.")
        else:
            print("\nCômodos da casa: \n")
            for c in self.__comodos:
                print(f"- {c.get_nome()}: {c.get_area()} m² ")
                print()

    def calcular_area_total(self):
        total = 0
        if not self.__comodos:
            print("\n Ainda não exite nenhum cômodo, crie um para fazer o cálculo da área total")
        else:
            for comodo in self.__comodos:
                total += comodo.get_area()    
        return total

def main():
    casa = None

    while True:
        print("\n=================MENU===================\n")
        print("1. - Criar nova casa")
        print("2. - Adicionar Cômodos a casa")
        print("3. - Listar cômodos da casa")
        print("4. - Calcular e exibir a área total")
        print("5. - Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ")
        
        if opcao == "1":
            if casa is None:
                casa = Casa()
                print("Casa criada com sucesso!")
                            
            else:
                print("A casa já foi criada! Só é possível criar uma casa!")
            
        elif opcao == "2":
            if casa is None:
                print("\nCriea casa primeiro, por favor!\n")
            else:
                nome = input("\nNome do cômodo: \n")
                area =  float(input("\náreado cômod em m²: \n"))

                casa.adicionar_comodo(nome, area)
                print("\nCômodo adicionado com sucesso!")
            
        elif opcao == "3":
            if casa is None:
                print("\nCriea casa primeiro, por favor!\n")
            else:
                casa.listar_comodos()
                        
           
        elif opcao == "4":
            if casa is None:
                print("\nCriea casa primeiro, por favor!\n")
            else:
                total = casa.calcular_area_total()
                print(f"Área total da casa em: {total:.2f} (m²)")
                      
        elif opcao == "5":
           
            print("Saindo...")
            break
           
        else:
            print("Opção inválida, tente novamente")

if __name__ == "__main__":
    main()




