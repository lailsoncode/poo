class Livro:
    def __init__(self, titulo, autor, isbn, copias_totais):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.copias_totais = copias_totais
        self.__emprestimos = []

    def get_emprestimos(self):
        return self.__emprestimos

    def emprestar(self):
        if self.get_disponibilidade > 0:
            self.copias_totais -= 1
            self.__emprestimos.append(1)
            return True
        else:
            return False
        
    def remover_emprestimo(self):
        if len(self.__emprestimos) > 0:
            self.__emprestimos.pop()
            self.copias_totais += 1
            return True
        else:
            return False
        
    def get_disponibilidade(self):
        return self.copias_totais
    
