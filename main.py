from services import servicos
from entities.cliente import Cliente
from entities.produto import Produto
from entities.pedido import Pedido

def cadastrar_cliente():
    print("Nome: ")
    nome = input()
    print("CPF: ")
    cpf = input()
    print("Email: ")
    email = input()
    servicos.todos_clientes.append(Cliente(nome, cpf, email))
    print("Cliente cadastrado com sucesso!\n")

def cadastrar_produto():
    try:
        print("Nome: ")
        nome = input()
        print("Preço: ")
        preco = float(input())
        print("Descrição: (Opcional, clique enter)")
        descricao = input()
        servicos.todos_produtos.append(Produto(nome, preco, descricao))
        print("Produto cadastrado com sucesso!\n")
    except ValueError:
        print("Erro: Campo 'preço' deve ser um número")
        print("Produto não salvo")
        print("--")
        cadastrar_produto()

def listar_produtos():
    print("====== LISTA DE PRODUTOS ======")
    if not servicos.todos_produtos:
        print("Nenhum produto cadastrado.\n")
    else:
        for i, p in enumerate(servicos.todos_produtos, 1):
            print(f"{i}. {p}")
        print()

def realizar_pedido():
    if not servicos.todos_clientes:
        print("Nenhum cliente cadastrado.\n")
        return
    if not servicos.todos_produtos:
        print("Nenhum produto cadastrado.\n")
        return

    print("====== LISTA DE CLIENTES ======")
    for i, c in enumerate(servicos.todos_clientes, 1):
        print(f"{i} - {c.nome}")
    try:
        idx_cliente = int(input("Escolha o número do cliente: ")) - 1
        cliente = servicos.todos_clientes[idx_cliente]
    except (ValueError, IndexError):
        print("Cliente inválido.\n")
        return

    print("====== LISTA DE PRODUTOS ======")
    for i, p in enumerate(servicos.todos_produtos, 1):
        print(f"{i} - {p}")
    print("Escolha os produtos pelo número (separados por vírgula): ")
    entrada = input()
    try:
        indices = [int(i.strip()) - 1 for i in entrada.split(",")]
        produtos = [servicos.todos_produtos[i] for i in indices]
        pedido = Pedido(cliente, produtos)
        servicos.todos_pedidos.append(pedido)
        print("Pedido realizado com sucesso!\n")
    except Exception as e:
        print("Erro ao realizar o pedido. Verifique a entrada.\n")

def ver_pedidos():
    print("====== PEDIDOS ======")
    if not servicos.todos_pedidos:
        print("Nenhum pedido registrado.\n")
    else:
        for p in servicos.todos_pedidos:
            print(p)
        print()

def main():
    while True:
        print("Seja Bem-vindo!")
        print("""
1 - Cadastro de Clientes
2 - Cadastro de Produtos
3 - Listar produtos
4 - Realizar pedidos
5 - Ver pedidos
6 - Sair
""")
        try:
            choice = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida, digite um número.\n")
            continue

        if choice == 1:
            cadastrar_cliente()
        elif choice == 2:
            cadastrar_produto()
        elif choice == 3:
            listar_produtos()
        elif choice == 4:
            realizar_pedido()
        elif choice == 5:
            ver_pedidos()
        elif choice == 6:
            print("Finalizando o sistema...")
            break
        else:
            print("Insira um número válido.\n")

if __name__ == "__main__":
    main()
