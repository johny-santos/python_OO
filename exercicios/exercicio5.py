class Impressora:
    def imprimir(self, documento):
        print(f"=========Impressão documento============")
        print(f"Título: {documento.titulo}")
        print(f"Conteúdo: {documento.conteudo}")

class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

def main():
    documentos = []
    impressora = Impressora()


    while True:
        print("\n=================MENU=====================\n")
        print("1 - Criar Documento")
        print("2 - Listar documentos ")
        print("3 - Imprimir documento ")
        print("4 - Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ")
        
        if opcao == "1":
            titulo = input("Digite o titulo do documento: ")

            conteudo = input("Esboçe o conteudo do seu documento abaixo: ")

            documento = Documento(titulo,conteudo)

            documentos.append(documento)
            
            print("Produto criado com sucesso!")
            
        elif opcao == "2":
            if not documentos:
                print("Não existe nenhum documento!")
            else:
                print("Lista de documentos: ")
                for i,doc in enumerate(documentos):
                    print(f"{i+1}. {doc.titulo}")

        elif opcao == "3":
            if not documentos:
               print("Nenhum documento disponível para impressão!")
            else:
                print("Escolha o número do documento para imprimir")
                for i,doc in enumerate(documentos):
                    print(f"{i+1}. {doc.titulo}")

                escolha = input("\n Número: ")

                if escolha.isdigit():
                    if 1 <= int(escolha) <= len(documentos):
                        impressora.imprimir(documentos[escolha - 1])
                    else:
                        print("Número inválido")
                else:
                    print("Entrada inválida. Digite um número!")    

        elif opcao == "4":
            print("Saindo...")
            break
           
        else:
            print("Opção inválida, tente novamente")

if __name__ == "__main__":
    main()





