class Personagem: 
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def atacar(self):
        print(f"\nPersonagem {self.nome} com o nível {self.nivel}, Atacou com tudo!\n")

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.forca = forca

    def atacar(self):
        print(f"\nO Guerreiro {self.nome}, com o nível {self.nivel} ataca com a força {self.forca}\n")
        

class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.mana = mana

    def atacar(self):
        print(f"O Mago {self.nome}, com o nível {self.nivel}, atacou com a mana de {self.mana}")

def main():

    personagem = Personagem("Naruto", 14)
    personagem.atacar()

    guerreiro = Guerreiro("Yu Zhong", 15, 15)
    guerreiro.atacar()

    mago = Mago("Selena", 15, 11)
    mago.atacar()

    lista_personagens = [personagem, guerreiro, mago]

    print("Ação dos personagens: ")
    for p in lista_personagens:
        p.atacar()

if __name__ == "__main__":
    main()

