class Pessoa:
    def __init__(self, nome=None, telefone='', idade=0, saldo=0.0):
        self.__nome = nome
        self.__telefone = telefone
        self.__idade = idade
        self.__saldo = saldo
   
    @property
    def nome(self):
        return self.__nome
   
    @nome.setter
    def nome(self, nome):
        self.__nome = nome




    @property
    def telefone(self):
        return self.__telefone
   
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
   
    @property
    def idade(self):
        return self.__idade
   
    @idade.setter
    def idade(self, idade):
        self.__idade = idade


    @property
    def saldo(self):
        return self.__saldo
   
   
    def depositar(self, valor):
        self.__saldo += valor


    def sacar(self, valor):
        self.__saldo -= valor


    def exibirDados(self):
        return ("Nome: " + str(self.__nome) + " - Saldo: " + str(self.__saldo))
