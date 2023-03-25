from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from ContaSalario import ContaSalario

contas = []

while True:
    print("\nMenu:\n")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")
    print("3 - Conta Salário")
    print("4 - Exibir Contas")
    print("5 - Sair")
    
    opcao = input("\nDigite a opção desejada: ")
    
    if opcao == "1":
        titular = input("Digite o nome do titular da conta: ")
        agencia = input("Digite o número da agência da conta: ")
        conta = input("Digite o número da conta: ")
        nova_conta = ContaCorrente(titular, agencia, conta)
        contas.append(nova_conta)
        print("\nConta corrente cadastrada com sucesso!")
    elif opcao == "2":
        titular = input("Digite o nome do titular da conta: ")
        agencia = input("Digite o número da agência da conta: ")
        conta = input("Digite o número da conta: ")
        nova_conta = ContaPoupanca(titular, agencia, conta)
        contas.append(nova_conta)
        print("\nConta poupança cadastrada com sucesso!")
    elif opcao == "3":
        titular = input("Digite o nome do titular da conta: ")
        agencia = input("Digite o número da agência da conta: ")
        conta = input("Digite o número da conta: ")
        nova_conta = ContaSalario(titular, agencia, conta)
        contas.append(nova_conta)
        print("\nConta salário cadastrada com sucesso!")
    elif opcao == "4":
        print("\nContas cadastradas:\n")
        for conta in contas:
            print(conta)
    elif opcao == "5":
        print("\nSaindo do programa...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
