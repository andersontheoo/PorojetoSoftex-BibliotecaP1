from models.livro import Livro
from models.membro import Membro
from models.emprestimo import Emprestimo

livros = []
membros = []
emprestimos = []

def adicionar_livro():
    id = len(livros) + 1
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    livros.append(Livro(id, titulo, autor, ano))
    print("📘 Livro adicionado com sucesso!")

def listar_livros():
    print("\n--- Lista de Livros ---")
    for livro in livros:
        status = "Disponível" if livro.esta_disponivel() else "Emprestado"
        print(f"[{livro._id}] {livro._titulo} - {status}")

def registrar_emprestimo():
    listar_livros()
    id_livro = int(input("ID do livro para emprestar: "))
    listar_membros()
    id_membro = int(input("ID do membro: "))

    livro = next((l for l in livros if l._id == id_livro), None)
    membro = next((m for m in membros if m._id == id_membro), None)

    if livro and membro and livro.esta_disponivel():
        livro.emprestar()
        emprestimo = Emprestimo(len(emprestimos) + 1, livro, membro)
        membro.adicionar_emprestimo(emprestimo)
        emprestimos.append(emprestimo)
        print("✅ Empréstimo realizado com sucesso!")
    else:
        print("⚠️ Livro indisponível ou membro inválido.")

def menu():
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Registrar Empréstimo")
        print("0. Sair")

        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            registrar_emprestimo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
