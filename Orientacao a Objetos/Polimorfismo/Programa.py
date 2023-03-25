from Pessoa import Pessoa
from PessoaFisica import PessoaFisica


pessoa1 = PessoaFisica(nome='Joseffe', cpf='38767654321')
pessoa2 = PessoaFisica(nome='Natan', cpf='45432312234')


pessoa1.depositar(100)
pessoa2.depositar(50)


pessoa1.sacar(20)
pessoa2.sacar(10)


print(pessoa1.exibirDados())
print(pessoa1.saldo)


print(pessoa2.exibirDados())
print(pessoa2.saldo)