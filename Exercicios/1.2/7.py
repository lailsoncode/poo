#7 Crie uma classe Pontuacao com um atributo pontos, inicializado  em 0, e dois métodos: adicionar_pontos(quantidade), que soma  quantidade ao total de pontos, e mostrar_pontos(), que imprime  a pontuação atual.

class Pontuacao:
    def __init__(self):
        self.pontos = 0

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade

    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}")

pontuacao = Pontuacao()
pontuacao.adicionar_pontos(10)
pontuacao.mostrar_pontos()