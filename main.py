import sys
import os
from datetime import date

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.livro import Livro
from models.membro import Membro
from models.emprestimo import Emprestimo

livros = []
membros = []
emprestimos = []

def adicionar_livro():
    try:
        id = int(input("ID do livro: "))
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))

        if any(l.get_id() == id for l in livros):
            print("❌ Já existe um livro com este ID!")
            return

        livro = Livro(id, titulo, autor, ano)
        livros.append(livro)
        print("✔ Livro adicionado com sucesso!")

    except ValueError:
        print("❌ Erro: valores inválidos!")


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for l in livros:
            print(l)


def atualizar_livro():
    try:
        id = int(input("ID do livro a atualizar: "))
        livro = next((l for l in livros if l.get_id() == id), None)

        if not livro:
            print("❌ Livro não encontrado!")
            return

        novo_titulo = input("Novo título (ENTER para manter): ")
        novo_autor = input("Novo autor (ENTER para manter): ")
        novo_ano = input("Novo ano (ENTER para manter): ")

        if novo_titulo:
            livro._titulo = novo_titulo
        if novo_autor:
            livro._autor = novo_autor
        if novo_ano:
            livro._ano = int(novo_ano)

        print("✔ Livro atualizado com sucesso!")

    except ValueError:
        print("❌ Ano inválido!")


def remover_livro():
    try:
        id = int(input("ID do livro a remover: "))
        livro = next((l for l in livros if l.get_id() == id), None)

        if not livro:
            print("❌ Livro não encontrado!")
            return

        if not livro.esta_disponivel():
            print("❌ Não é possível remover um livro emprestado!")
            return

        livros.remove(livro)
        print("✔ Livro removido com sucesso!")

    except ValueError:
        print("❌ ID inválido!")


def adicionar_membro():
    try:
        id = int(input("ID do membro: "))
        nome = input("Nome: ")
        email = input("Email: ")

        if any(m.get_id() == id for m in membros):
            print("❌ Já existe um membro com esse ID!")
            return

        membro = Membro(id, nome, email)
        membros.append(membro)
        print("✔ Membro adicionado com sucesso!")

    except ValueError:
        print("❌ ID inválido!")


def listar_membros():
    if not membros:
        print("Nenhum membro cadastrado.")
        return

    for m in membros:
        print(f"[{m.get_id()}] {m.get_nome()} - {m.get_email()}")


def atualizar_membro():
    try:
        id = int(input("ID do membro a atualizar: "))
        membro = next((m for m in membros if m.get_id() == id), None)

        if not membro:
            print("❌ Membro não encontrado!")
            return

        nome = input("Novo nome (ENTER para manter): ")
        email = input("Novo email (ENTER para manter): ")

        if nome:
            membro._nome = nome
        if email:
            membro._email = email

        print("✔ Membro atualizado com sucesso!")

    except ValueError:
        print("❌ ID inválido!")


def remover_membro():
    try:
        id = int(input("ID do membro a remover: "))
        membro = next((m for m in membros if m.get_id() == id), None)

        if not membro:
            print("❌ Membro não encontrado!")
            return

        if any(e._membro.get_id() == membro.get_id() and e._data_dev is None for e in emprestimos):
            print("❌ Membro possui empréstimos em aberto!")
            return

        membros.remove(membro)
        print("✔ Membro removido com sucesso!")

    except ValueError:
        print("❌ ID inválido!")

def emprestar_livro():
    try:
        id_livro = int(input("ID do livro: "))
        id_membro = int(input("ID do membro: "))

        livro = next((l for l in livros if l.get_id() == id_livro), None)
        membro = next((m for m in membros if m.get_id() == id_membro), None)

        if not livro:
            print("❌ Livro não encontrado!")
            return
        if not membro:
            print("❌ Membro não encontrado!")
            return

        if not livro.esta_disponivel():
            print("❌ O livro já está emprestado!")
            return

        livro.emprestar()
        emprestimo = Emprestimo(len(emprestimos)+1, livro, membro)
        emprestimos.append(emprestimo)
        membro.adicionar_emprestimo(emprestimo)

        print("✔ Livro emprestado com sucesso!")

    except ValueError:
        print("❌ ID inválido!")


def devolver_livro():
    try:
        id_livro = int(input("ID do livro para devolver: "))

        emprestimo = next((e for e in emprestimos if e._livro.get_id() == id_livro and e._data_dev is None), None)

        if not emprestimo:
            print("❌ Este livro não está emprestado!")
            return

        emprestimo.devolver()
        print("✔ Livro devolvido com sucesso!")

    except ValueError:
        print("❌ ID inválido!")


def menu():
    while True:
        print("\n====== MENU BIBLIOTECA ======")
        print("1 - Adicionar Livro")
        print("2 - Listar Livros")
        print("3 - Atualizar Livro")
        print("4 - Remover Livro")
        print("5 - Adicionar Membro")
        print("6 - Listar Membros")
        print("7 - Atualizar Membro")
        print("8 - Remover Membro")
        print("9 - Emprestar Livro")
        print("10 - Devolver Livro")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("❌ Digite um número válido!")
            continue

        if opcao == 1:
            adicionar_livro()
        elif opcao == 2:
            listar_livros()
        elif opcao == 3:
            atualizar_livro()
        elif opcao == 4:
            remover_livro()
        elif opcao == 5:
            adicionar_membro()
        elif opcao == 6:
            listar_membros()
        elif opcao == 7:
            atualizar_membro()
        elif opcao == 8:
            remover_membro()
        elif opcao == 9:
            emprestar_livro()
        elif opcao == 10:
            devolver_livro()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    menu()