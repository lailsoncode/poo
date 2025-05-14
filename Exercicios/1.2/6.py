#6 Crie uma classe Personagem com um atributo nome e um  método dizer_nome() que imprime "Meu nome é {nome}".  Instancie um personagem e teste o método.

class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def dizer_nome(self):
        print(f"Meu nome é {self.nome}")

personagem = Personagem("Heroi")
personagem.dizer_nome()