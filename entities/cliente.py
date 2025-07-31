class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def __str__(self):
        return f"{self.nome} - {self.email}"
