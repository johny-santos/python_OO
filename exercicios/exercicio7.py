class comodo:
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
        self.__area = area

class Casa:
    def __init__(self):
        self.__comodos = [] 

    def adicionar_comodo(self, nome, area):
        novo_comodo = comodo(nome, area)

        self.__comodos.append(novo_comodo)
        print(f"O cômodo: '{nome}', foi adicionado com sucesso!")

    def listar_comodos(self):
        if not self.__comodos:
            print("\nNenhum cômodo encontrado, acrescente um para v~e-los aqui.")
        else:
            print("Cômodos da casa: ")
            for c in self.__comodos:
                print(f"- {c.get_nome()}: {c.get_area()}")

    def calcular_area_total(self):
        total = 0
        if not self.__comodos:
            print("\n Ainda não exite nenhum cômodo, crie um para fazer o cálculo da área total")
        else:
            for comodo in self.__comodos:
                total += comodo.get_area()    
        return total




