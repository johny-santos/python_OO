class Progressao_Aritmetica:
    def __init__(self, n, a1, r):
        self.__n = n
        self.__a1 = a1
        self.r__r = r

    def gerar_termos(self):
        """Gera e retorna todos os termos da P.A. em uma lista."""
        termos = []
        for i in range(self.__n): #tamanho de termos 
            an = self.__a1 + self.__r * i
            termos.append(an)
        return termos

    def calcular_soma(self, termos):
        """Calcula a soma usando a fórmula S = n * (a1 + an) / 2."""
        an = termos[-1] # O último termo da lista é o 'an'
        soma = self.__n * (self.__a1 + an) / 2
        return soma

def main():
    print("\n========================= Gerador de progressão Aritmética =========================\n")

    n = int(input("Digite o número de termos da Progressão Aritmética (n): "))
    a1 = float(input("Digite o primeiro termo da progressão (a1): "))
    r = float(input("Digite a Razão (r): "))


    pa = Progressao_Aritmetica(n, a1, r)

    lista_tudo = pa.gerar_termos()

    contador = 1
    for termo in lista_tudo:
        print(f"Os termo {contador} da P.A é respectivamente {termo}")

    mostra_calculo = pa.calcular_soma()
    
    print(f"O valor do cálculo {n} é = {mostra_calculo}")

if __name__ == "__main__":
    main()