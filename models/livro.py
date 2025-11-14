class Livro:
    def __init__(self, id, titulo, autor, ano, emprestado=False):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._emprestado = emprestado  

    def emprestar(self):
        if not self._emprestado:
            self._emprestado = True
            return True
        return False

    def devolver(self):
        self._emprestado = False

    def esta_disponivel(self):
        return not self._emprestado

    def to_dict(self):
        return {
            "id": self._id,
            "titulo": self._titulo,
            "autor": self._autor,
            "ano": self._ano,
            "emprestado": self._emprestado
        }

    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_ano(self):
        return self._ano

    def __str__(self):
        status = "Disponível" if self.esta_disponivel() else "Emprestado"
        return f"[{self._id}] {self._titulo} - {self._autor} ({self._ano}) | {status}"
