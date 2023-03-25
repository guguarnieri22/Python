from Pessoa import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, nome=None, telefone='', idade=0, saldo=0.0, cpf=''):
        super().__init__(nome, telefone, idade, saldo)
        self.__cpf = cpf


    @property
    def cpf(self):
        return self.__cpf
   
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf


    def exibirDados(self):
        return super().exibirDados() + " - Cpf: " + str(self.__cpf)
   
    def depositar(self, valor):
        valor = valor + 0.10
        super().depositar(valor)