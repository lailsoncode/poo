#5 Crie uma classe Menu com três métodos: iniciar_jogo(),  mostrar_opcoes(), e sair(). Cada método deve imprimir uma  mensagem correspondente. Instancie a classe e teste os  métodos.

class Menu:
    def iniciar_jogo(self):
        print("Iniciando o jogo...")

    def mostrar_opcoes(self):
        print("Mostrando opções...")

    def sair(self):
        print("Saindo do jogo...")

menu = Menu()
menu.iniciar_jogo()
menu.mostrar_opcoes()
menu.sair()