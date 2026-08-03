class Criptografar_Frase:
    def __init__(self, texto):
        self.texto = texto

    def criptografar(self):
        texto_cripto = self.texto.upper()

        texto_cripto = texto_cripto.replace('A', '4')
        texto_cripto = texto_cripto.replace('E', '3')
        texto_cripto = texto_cripto.replace('I', '1')
        texto_cripto = texto_cripto.replace('O', '0')
        texto_cripto = texto_cripto.replace('U', '8')

        return texto_cripto

def main():
    texto = input("Digite um texto qualquer")

    criptografar = Criptografar_Frase(texto)

    resultado = criptografar.criptografar()

    print(f"{resultado}")


if __name__ == "__main__": 
    main()