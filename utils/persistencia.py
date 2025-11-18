import json
import os
from typing import Dict, Any

CAMINHO = "data/banco.json"

def carregar_dados() -> Dict[str, Any]:
    if not os.path.exists(CAMINHO):
        dados_iniciais = {"livros": [], "membros": [], "emprestimos": []}
        salvar_dados(dados_iniciais)
        return dados_iniciais
    with open(CAMINHO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados: Dict[str, Any]) -> None:
    with open(CAMINHO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

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
    return carregar_dados()["livros"]

def listar_membros():
    return carregar_dados()["membros"]

def listar_emprestimos():
    return carregar_dados()["emprestimos"]

def atualizar_livro(livro_id: int, campos: Dict[str, Any]) -> bool:
    dados = carregar_dados()
    for i, l in enumerate(dados["livros"]):
        if l["id"] == livro_id:
            dados["livros"][i].update(campos)
            salvar_dados(dados)
            return True
    return False

def atualizar_membro(membro_id: int, campos: Dict[str, Any]) -> bool:
    dados = carregar_dados()
    for i, m in enumerate(dados["membros"]):
        if m["id"] == membro_id:
            dados["membros"][i].update(campos)
            salvar_dados(dados)
            return True
    return False

def atualizar_emprestimo(emp_id: int, campos: Dict[str, Any]) -> bool:
    dados = carregar_dados()
    for i, e in enumerate(dados["emprestimos"]):
        if e["id"] == emp_id:
            dados["emprestimos"][i].update(campos)
            salvar_dados(dados)
            return True
    return False

def remover_livro(livro_id: int) -> bool:
    dados = carregar_dados()
    for i, l in enumerate(dados["livros"]):
        if l["id"] == livro_id:
            dados["livros"].pop(i)
            salvar_dados(dados)
            return True
    return False

def remover_membro(membro_id: int) -> bool:
    dados = carregar_dados()
    for i, m in enumerate(dados["membros"]):
        if m["id"] == membro_id:
            dados["membros"].pop(i)
            salvar_dados(dados)
            return True
    return False

def remover_emprestimo(emp_id: int) -> bool:
    dados = carregar_dados()
    for i, e in enumerate(dados["emprestimos"]):
        if e["id"] == emp_id:
            dados["emprestimos"].pop(i)
            salvar_dados(dados)
            return True
    return False
