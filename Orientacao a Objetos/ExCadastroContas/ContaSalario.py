from Conta import Conta

class ContaSalario(Conta):
    def __init__(self, titular, agencia, conta):
        super().__init__(titular, agencia, conta)

    def __str__(self):
        return f"Conta Salário\n{super().__str__()}"