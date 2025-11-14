import json
import os

CAMINHO = "data/banco.json"

def salvar_dados(dados):
    with open(CAMINHO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_dados():
    if not os.path.exists(CAMINHO):
        dados_iniciais = {
            "livros": [],
            "membros": [],
            "emprestimos": []
        }
        salvar_dados(dados_iniciais)
        return dados_iniciais

    with open(CAMINHO, "r", encoding="utf-8") as f:
        return json.load(f)

def adicionar_livro(livro):
    dados = carregar_dados()
    dados["livros"].append(livro.to_dict())
    salvar_dados(dados)

def adicionar_membro(membro):
    dados = carregar_dados()
    dados["membros"].append(membro.to_dict())
    salvar_dados(dados)

def adicionar_emprestimo(emprestimo):
    dados = carregar_dados()
    dados["emprestimos"].append(emprestimo.to_dict())
    salvar_dados(dados)


def listar_livros():
    dados = carregar_dados()
    return dados["livros"]

def listar_membros():
    dados = carregar_dados()
    return dados["membros"]

def listar_emprestimos():
    dados = carregar_dados()
    return datos["emprestimos"]
