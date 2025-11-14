class Membro:
    def __init__(self, id, nome, email):
        self._id = id
        self._nome = nome
        self._email = email
        self._emprestimos = []  

    def adicionar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        return self._emprestimos

    def to_dict(self):
        return {
            "id": self._id,
            "nome": self._nome,
            "email": self._email,
            "emprestimos": self._emprestimos
        }

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email