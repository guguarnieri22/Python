class Conta:
    def __init__(self, titular, agencia, conta):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta



    def __str__(self):
        return f"Titular: {self.titular}\nAgência: {self.agencia}\nConta: {self.conta}"