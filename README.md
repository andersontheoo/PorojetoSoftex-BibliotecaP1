# Sistema de Gestão de Biblioteca (CLI)

## 1. Objetivo
Desenvolver um sistema em linha de comando (CLI) para gerir livros, membros e empréstimos de uma biblioteca.

---

## 2. Requisitos Funcionais (RF)
| Código | Descrição |
|--------|------------|
| **RF01** | Cadastrar livros com título, autor, ano e tipo. |
| **RF02** | Listar todos os livros cadastrados. |
| **RF03** | Buscar livros por título. |

---

## 3. Requisitos Não Funcionais (RNF)
| Código | Descrição |
|--------|------------|
| **RNF01** | O sistema deve funcionar em linha de comando (CLI). |
| **RNF02** | O sistema deve usar persistência em JSON. |

---

## 4. Diagrama de Classes

+------------------+        +-------------------+        +-------------------+
|      Livro       |<>------|    Emprestimo     |------<>|      Membro       |
+------------------+        +-------------------+        +-------------------+
| - id: int        |        | - id: int         |        | - id: int         |
| - titulo: str    |        | - livro: Livro    |        | - nome: str       |
| - autor: str     |        | - membro: Membro  |        | - email: str      |
| - ano: int       |        | - data_emp: date  |        | - emprestimos: [] |
+------------------+        | - data_dev: date  |        +-------------------+
        ^                   +-------------------+
        |
        |--- LivroFisico
        |--- LivroDigital
