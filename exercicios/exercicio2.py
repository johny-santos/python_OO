class StringUsuario:
    def __init__(self, texto):
        self.texto = texto

    def numero_caracteres(self):
        return len(self.texto)

    def maiuscula(self):
        return self.texto.upper()

    def minuscula(self):
        return self.texto.lower()

    def numero_vogais(self):
        vogais = "aeiouAEIOU"

        return sum(1 for letra in self.texto if letra in vogais)

    def contem_ifb(self):
        return "ifb" in self.texto.lower()

def main():
    entrada = input("Digite um texto: ")
    
    processador = StringUsuario(entrada)
    
    print(f"O número de caracteres da string: {processador.numero_caracteres()}")
    print(f"A string com todas suas letras em maiúsculo: {processador.maiuscula()}")
    print(f"A string com todas suas letras em minúsculo: {processador.minuscula()}")
    print(f"O número de vogais da string: {processador.numero_vogais()}")
    
    if processador.contem_ifb():
        print("A substring 'IFB' aparece no texto? Sim")
    else:
        print("A substring 'IFB' aparece no texto? Não")


if __name__ == "__main__":
    main()
