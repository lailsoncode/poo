#9 Crie uma classe Jogador com um atributo energia, inicializado  em 50. Adicione métodos recuperar_energia(quantidade) e  usar_energia(quantidade). Se a energia for menor que 0,  imprima "Sem energia suficiente!".

class Jogador:
    def __init__(self):
        self.energia = 50

    def recuperar_energia(self, quantidade):
        self.energia += quantidade

    def usar_energia(self, quantidade):
        self.energia -= quantidade
        if self.energia < 0:
            print("Sem energia suficiente!")

jogador = Jogador()
jogador.usar_energia(20)
jogador.recuperar_energia(30)
jogador.usar_energia(70)