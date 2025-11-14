from datetime import date

class Emprestimo:
    def __init__(self, id, livro, membro):
        self._id = id
        self._livro = livro
        self._membro = membro
        self._data_emp = date.today()
        self._data_dev = None

    def devolver(self):
        self._data_dev = date.today()
        self._livro.devolver()
