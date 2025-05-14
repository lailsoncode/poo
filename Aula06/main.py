# Implemente as seguintes classes:
# Veiculo (classe base) com o método mover().
# Bicicleta (subclasse de Veiculo) com o método adicional pedalar().
# Onibus (subclasse de Veiculo) com o método adicional embarcar_passageiros().
# Crie objetos das três classes e chame todos os métodos disponíveis para cada objeto.

class Veiculo:
    def mover(self):
        print("O veículo está se movendo.")

class Bicicleta(Veiculo):
    def pedalar(self):

class Onibus(Veiculo):
    def embarcar_passageiros(self):
