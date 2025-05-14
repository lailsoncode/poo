class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        alvo.tomar_dano(10)
        print(f"{self.nome} atacou {alvo.nome}!")
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} agora tem {self.vida} de vida.")
inimigo = Inimigo("Goblin")
personagem = Personagem("Heroi")
inimigo.atacar(personagem)