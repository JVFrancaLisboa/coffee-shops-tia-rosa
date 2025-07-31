class Pedido:
    def __init__(self, cliente, produtos):
        self.cliente = cliente
        self.produtos = produtos

    def __str__(self):
        produtos_str = ", ".join(p.nome for p in self.produtos)
        return f"Pedido de {self.cliente.nome}: {produtos_str}"
