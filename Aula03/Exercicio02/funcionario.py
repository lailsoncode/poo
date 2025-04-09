# Crie uma classe Funcionario com os seguintes elementos:
# Atributos: nome, id_funcionario, salario_base, bonus, faltas
# Métodos: registrar_falta(), adicionar_bonus(), recalcular_bonus(), get_id(), calcular_salario(), resumo()

class Funcionario:
    def __init__(self, nome, id_funcionario, salario_base):
        self.nome = nome
        self.id_funcionario = id_funcionario
        self.salario_base = salario_base
        self.__bonus = 0
        self.__faltas = 0

    def registrar_falta(self):
        self.__faltas += 1

    def adicionar_bonus(self, valor):
        self.__bonus += valor
        return self.salario_base + self.__bonus
    
    def recalcular_bonus(self):
        if self.__faltas > 0:
            self.__bonus -= self.__faltas * 100
        return self.__bonus
    
    def get_id(self):
        return self.id_funcionario

    def calcular_salario(self):
        self.salario_base = self.salario_base + self.__bonus - (self.__faltas * 100)
        return self.salario_base
    
    def resumo(self):
        return f"Nome: {self.nome}, ID: {self.id_funcionario}, Salário Base: {self.calcular_salario()}, Bonus: {self.__bonus}, Faltas: {self.__faltas}"