# Aula 2 - 26/03/2025
# Classes e Objetos

class Garrafa:
    def __init__(self,value1):
        self.modelo = value1
        self.cor = None
        self.volume = None
        self.estampa = None
        self.preco = None

garrafa1 = Garrafa("Atack On Titan")

print (garrafa1.modelo)


class Livro:
    def __init__(self, valor1, valor2, valor3, valor4, valor5):
        self.capa = valor1
        self.titulo = valor2
        self.tipo = valor3
        self.preco = valor4
        self.codigo = valor5

livro1 = Livro("Capa Dura","O Pequeno Principe","Romance","19,90","COD001")

print('Tipo de Capa: ' + livro1.capa)
print('Titulo: ' + livro1.titulo)
print('Gênero: ' + livro1.tipo)
print('Preço: ' + livro1.preco)
print('Código: ' + livro1.codigo)


class Conta:
    def __init__(self, valor1, valor2, valor3, valor4):
        self.nome = valor1
        self.numero = valor2
        self.agencia = valor3
        self.saldo = valor4

conta1 = Conta("João","123456","0001","1000")

print('Nome: ' + conta1.nome)
print('Número: ' + conta1.numero)
print('Agência: ' + conta1.agencia)
print('Saldo: ' + conta1.saldo)


class Tarefa:
    def __init__(self, valor1, valor2, valor3, valor4):
        self.titulo = valor1
        self.descricao = valor2
        self.prioridade = valor3
        self.status = valor4

tarefa1 = Tarefa("Estudar","Estudar Python","Alta","Pendente")

print('Título: ' + tarefa1.titulo)
print('Descrição: ' + tarefa1.descricao)
print('Prioridade: ' + tarefa1.prioridade)
print('Status: ' + tarefa1.status)


class Termostato:
    def __init__(self, valor1, valor2, valor3, valor4, valor5):
        self.temperatura = valor1
        self.umidade = valor2
        self.horario = valor3
        self.data = valor4
        self.status = valor5

termostato1 = Termostato("25","50","12:00","01/01/2021","Ligado")

print('Temperatura: ' + termostato1.temperatura)
print('Umidade: ' + termostato1.umidade)
print('Horário: ' + termostato1.horario)
print('Data: ' + termostato1.data)
print('Status: ' + termostato1.status)


class DNA:
    def __init__(self, valor1, valor2, valor3, valor4, valor5):
        self.nome = valor1
        self.tipo = valor2
        self.tamanho = valor3
        self.origem = valor4
        self.status = valor5

dna1 = DNA("DNA1","RNA","1000","Origem","Ativo")

print('Nome: ' + dna1.nome)
print('Tipo: ' + dna1.tipo)
print('Tamanho: ' + dna1.tamanho)
print('Origem: ' + dna1.origem)
print('Status: ' + dna1.status)


class Pixel:
    def __init__(self, valor1, valor2, valor3, valor4, valor5):
        self.cor = valor1
        self.brilho = valor2
        self.tamanho = valor3
        self.resolucao = valor4
        self.status = valor5

pixel1 = Pixel("Vermelho","50","10x10","1080p","Ativo")

print('Cor: ' + pixel1.cor)
print('Brilho: ' + pixel1.brilho)
print('Tamanho: ' + pixel1.tamanho)
print('Resolução: ' + pixel1.resolucao)
print('Status: ' + pixel1.status)