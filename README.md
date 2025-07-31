# ☕ Coffee Shops Tia Rosa - Sistema de Gerenciamento (Python)

Este repositório contém o sistema desenvolvido em Python para a cafeteria **Coffee Shops Tia Rosa**, como parte da atividade da disciplina de programação. O objetivo principal é criar uma solução simples, funcional e acessível para melhorar a organização interna da cafeteria, respeitando a realidade tecnológica da equipe atual.

## 📌 Objetivo do Projeto

Criar um sistema de gerenciamento básico com funcionalidades como:

- Cadastro de produtos
- Cadastro de clientes
- Registro de pedidos
- Listagem de dados

## 🧩 Estrutura do Projeto

O projeto está organizado da seguinte forma:

cafeteria/
├── entities/

│ ├── cliente.py # Classe Cliente

│ ├── produto.py # Classe Produto

│ └── pedido.py # Classe Pedido

├── services/

│ └── servicos.py # Listas globais de produtos e clientes

├── main.py # Execução principal e simulação do sistema


## ✅ Funcionalidades

- `Cliente`: armazena nome, CPF e e-mail.
- `Produto`: armazena nome, preço e descrição.
- `Pedido`: associa cliente a uma lista de produtos.
- `Serviços`: armazena produtos e clientes globalmente.
- `main.py`: executa testes e simula o uso do sistema via terminal.

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- Programação orientada a objetos
- Tipagem com `list[Tipo]` e `@property`
- Estrutura modular com pacotes

## 📚 Aprendizados

Durante o desenvolvimento do sistema, foram praticados os seguintes conceitos:

- Organização de projetos em pacotes (`entities`, `services`)
- Uso de classes, atributos e métodos
- Listas tipadas para armazenamento de objetos
- Simulação de lógica de negócio simples
- Importações e reutilização de código em Python


## 👨‍🏫 Requisitos Atendidos

- [x] Código em Python comentado e funcional
- [x] Interface em linha de comando
- [x] Uso de listas, classes e funções
- [x] Organização clara e lógica
- [x] Relatório com prints e descrição do sistema

---

> **Desenvolvido por [Josué Vítor França Lisboa]**
>
> Projeto individual da disciplina de Programação Python – Prof. Francisco Lima
