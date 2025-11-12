class Livro:
    def __init__(self, id, titulo, autor, ano):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._emprestado = False  

    def emprestar(self):
        if not self._emprestado:
            self._emprestado = True
            return True
        return False

    def devolver(self):
        self._emprestado = False

    def esta_disponivel(self):
        return not self._emprestado
