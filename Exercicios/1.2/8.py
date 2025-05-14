#8 Crie uma classe Personagem com um atributo vida, inicializado  em 100. Adicione um método tomar_dano(dano), que reduz a  vida do personagem pelo valor passado como parâmetro. Se a  vida chegar a 0, imprima "Game Over!".
class Personagem:
    def __init__(self):
        self.vida = 100

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print("Game Over!")

personagem = Personagem()
personagem.tomar_dano(50)
personagem.tomar_dano(60)