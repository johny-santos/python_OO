class Biblioteca:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.livros = []
        
    def criar_livro(self, titulo, ano, autor):
        livro = Livro(titulo, ano, autor)

        self.livros.append(livro)

        return livro

    def listar_livros(self):
        print(f"Livros disponíveis na biblioteca {self.nome}")
        for livro in self.listar_livros:
            print(f"Título livro: {livro.titulo}, Ano: {livro.ano}, Autor: {livro.autor.nome}")

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor 
                    
class Autor:
    def __init__(self, nome_autor, nacionalidade):
        self.nome_autor =  nome_autor
        self.nacionalidade = nacionalidade

class Usuario:
    def __init__(self, nome_usuario, biblioteca):
        self.nome_usuario = nome_usuario
        self.biblioteca = biblioteca

    def exibir_info_usuario(self):
        print(f"Nome usuário: {self.nome_usuario}")
        print(f"Biblioteca associada: {self.biblioteca}")

    def emprestar_livro(self, livro):

        if livro in self.biblioteca.livros:
            print(f"{self.nome_usuario} pegou emprestqado o livro {livro.titulo}")
        else:
            print(f"Livro: {livro.titulo} não está disponível na biblioteca! {self.biblioteca.nome}")




def main():
    autor1 = Autor("Machado de Asis", "Brasileiro")
    autor = Autor("J.K Rowling", "Britânica")

    biblioteca = Biblioteca("Bin")

    livro1 = biblioteca.criar_livro(Livro("A causa Secreta", 1799, autor1)) 
    livro2 = biblioteca.criar_livro(Livro("Harry porra", 2000, autor))

    biblioteca.listar_livros()

  
    usuario = Usuario("Carlos", biblioteca) 

    usuario.emprestar_livro(livro1)



if __name__ == "__main__":
    main()