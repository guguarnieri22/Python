from Pessoa import Pessoa
from PessoaFisica import PessoaFisica


pessoa1 = PessoaFisica('Joseffe')
pessoa2 = PessoaFisica('Natan')


pessoa1.depositar(100)
pessoa2.depositar(50)


pessoa1.sacar(20)
pessoa2.sacar(10)


print(pessoa1.exibirDados())
print(pessoa1.saldo)


print(pessoa2.exibirDados())
print(pessoa2.saldo)
