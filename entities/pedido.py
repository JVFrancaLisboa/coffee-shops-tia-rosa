from entities.cliente import Cliente
from produto import Produto

class Pedido:
    def __init__(self, cliente: Cliente, produtos: list[Produto]):
        self.cliente = cliente
        self.produtos = produtos

    def __str__(self):
        produtos_str = ", ".join(str(p) for p in self.produtos)
        return f"Pedido de {self.Cliente.nome}: [{produtos_str}]"