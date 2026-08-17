class Paticipante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
    def emitirCertificado(self):
        return f"Certificado emitido para o participante {self.nome}."
    
class Aluno(Paticipante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.curso = curso

    def emitirCertificado(self):
        print(f"Certificado de conclusão do Aluno: {self.nome}, no curso: {self.curso} obrigado por sua confiança!")
    
class Instrutor(Paticipante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.especialidade = especialidade

    def emitirCertificado(self):
        print(f"Certificado de conclusão do Instrutor: {self.nome}, obrigado por sua colaboração!")
    
def main():
    participantes = []

    while True:
        print("\n=================MENU===================\n")
        print("1. - Cadastrar participantes")
        print("2. - Listar participantes")
        print("3. - Emitir certificados")
        print("0. - Sair")
        
        opcao = input("\nEscolha uma opção (0-3): \n")
        
        if opcao == "1":
            while True:
                print("\n1. - Cadastrar Aluno\n")
                print("\n2. - Cadastrar instrutor\n")
                print("\n0. - Sair\n")
                

                opcao2 = input("\nEscolha uma opcao entre 0-2: \n")

                if opcao2 == "1":
                    nome_aluno = input("\nDigite o nome do Aluno(a): \n")

                    email_aluno =  input("\nDigite o E-mail do Aluno(a): \n")

                    curso_aluno = input("\nDigite qual o referido Aluno(a) faz: \n")

                    novo_aluno = Aluno(nome_aluno, email_aluno, curso_aluno)

                    participantes.append(novo_aluno)

                    print("\nAluno(a) cadastrado(a) com sucesso!\n")

                elif opcao2 == "2":
                    nome_instrutor = input("\nDigite o nome do Instrutor(a): \n")
                    
                    email_instrutor =  input("\nDigite o E-mail do Instrutor(a): \n")

                    especialidade_instrutor = input("\nDigite a especialidade do instrutor(a): \n")

                    novo_instrutor = Instrutor(nome_instrutor, email_instrutor, especialidade_instrutor)

                    participantes.append(novo_instrutor)
                    
                    print("\nInstrutor(a) cadastrado(a) com sucesso!\n")

                elif opcao2 == "0":
                    print("Voltando...")
                    break   

                else:
                    print("Opção inválida, tente novamente!") 
            
        elif opcao == "2":
            if not participantes:
                print("\nNenhum participante encontrado!\n Cadastre algum participante e você poderá vê-los aqui.")
            else:
                for p in participantes:

                    print(f"Nome: {p.nome}")
                    print(f"E-mail: {p.email}")

        elif opcao == "3":
            if not participantes:
                print("\nNenhum participante encontrado!\n Cadastre algum participante e você poderá vê-los aqui.")
            else:
                print("Certificados: ")
                for p in participantes:
                    p.emitirCertificado()
                                      
        elif opcao == "0":
           
            print("Saindo...")
            break
           
        else:
            print("Opção inválida, tente novamente")

if __name__ == "__main__":
    main()
    

