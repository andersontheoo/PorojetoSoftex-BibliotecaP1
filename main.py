from models.livro import Livro
from models.membro import Membro
from models.emprestimo import Emprestimo
from utils.persistencia import (
    carregar_dados,
    adicionar_livro,
    adicionar_membro,
    adicionar_emprestimo,
    listar_livros as ler_livros,
    listar_membros as ler_membros,
    listar_emprestimos as ler_emprestimos
)

def get_livro_por_id(id):
    livros = ler_livros()
    for l in livros:
        if l["id"] == id:
            return Livro(**l)
    return None

def get_membro_por_id(id):
    membros = ler_membros()
    for m in membros:
        if m["id"] == id:
            return Membro(**m)
    return None

def adicionar_livro_menu():
    dados = carregar_dados()
    novo_id = len(dados["livros"]) + 1

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano: ").strip()

    livro = Livro(novo_id, titulo, autor, ano)
    adicionar_livro(livro)

    print("📘 Livro adicionado com sucesso!")

def adicionar_membro_menu():
    dados = carregar_dados()
    novo_id = len(dados["membros"]) + 1

    nome = input("Nome: ").strip()
    email = input("Email: ").strip()

    membro = Membro(novo_id, nome, email)
    adicionar_membro(membro)

    print("👤 Membro adicionado com sucesso!")

def listar_livros_menu():
    livros = ler_livros()
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\n--- Lista de Livros ---")
    for l in livros:
        print(f"[{l['id']}] {l['titulo']} - {l['autor']} ({l['ano']})")

def listar_membros_menu():
    membros = ler_membros()
    if not membros:
        print("Nenhum membro cadastrado.")
        return

    print("\n--- Lista de Membros ---")
    for m in membros:
        print(f"[{m['id']}] {m['nome']} - {m['email']}")

def registrar_emprestimo():
    dados = carregar_dados()

    if not dados["livros"] or not dados["membros"]:
        print("⚠️ É necessário ter pelo menos 1 livro e 1 membro.")
        return

    listar_livros_menu()
    id_livro = int(input("ID do livro: "))
    livro = get_livro_por_id(id_livro)

    if not livro:
        print("Livro não encontrado.")
        return

    if not livro.esta_disponivel():
        print("⚠️ Livro já está emprestado.")
        return

    listar_membros_menu()
    id_membro = int(input("ID do membro: "))
    membro = get_membro_por_id(id_membro)

    if not membro:
        print("Membro não encontrado.")
        return

    livro.emprestar()
    novo_id = len(dados["emprestimos"]) + 1
    emp = Emprestimo(novo_id, livro, membro)

    adicionar_emprestimo(emp)

    print("✅ Empréstimo registrado!")

def devolver_livro():
    emprestimos = ler_emprestimos()

    abertos = [e for e in emprestimos if e["data_dev"] is None]

    if not abertos:
        print("Nenhum empréstimo em aberto.")
        return

    print("\n--- Empréstimos em aberto ---")
    for e in abertos:
        print(f"[{e['id']}] Livro: {e['livro']['titulo']} | Membro: {e['membro']['nome']}")

    id_emp = int(input("ID do empréstimo para devolver: "))

    emprestimo = next((x for x in abertos if x["id"] == id_emp), None)

    if not emprestimo:
        print("Empréstimo não encontrado.")
        return

    emp_obj = Emprestimo.from_dict(emprestimo)
    emp_obj.devolver()

    dados = carregar_dados()
    for i, e in enumerate(dados["emprestimos"]):
        if e["id"] == id_emp:
            dados["emprestimos"][i] = emp_obj.to_dict()
            break
    
    for l in dados["livros"]:
        if l["id"] == emprestimo["livro"]["id"]:
            l["emprestado"] = False

    from utils.persistencia import salvar_dados
    salvar_dados(dados)

    print("📗 Livro devolvido com sucesso!")


def menu():
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Adicionar Membro")
        print("4. Listar Membros")
        print("5. Registrar Empréstimo")
        print("6. Devolver Livro")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_livro_menu()
        elif opcao == "2":
            listar_livros_menu()
        elif opcao == "3":
            adicionar_membro_menu()
        elif opcao == "4":
            listar_membros_menu()
        elif opcao == "5":
            registrar_emprestimo()
        elif opcao == "6":
            devolver_livro()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()