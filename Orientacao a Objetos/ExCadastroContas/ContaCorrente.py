from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, agencia, conta):
        super().__init__(titular, agencia, conta)
        

    def __str__(self):
        return f"Conta Corrente\n{super().__str__()}"