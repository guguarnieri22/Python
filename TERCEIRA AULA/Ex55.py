num = []
pos = -1


qtde = int(input("Insira a quantidade de valores: "))

while (qtde > 20 or qtde <= 0):
    print("De 1 à 20!")
    qtde = int(input("Digite o valor de 1 à 20 novamente: "))

for i in range(0, qtde, 1):
    x = int(input("Digite um numero: "))
    num.append(x)

posicao = int(input("Digite o valor que queira saber o array: "))

for i in range(0, qtde, 1):
    if (num[i] == posicao):
        pos = 1

if pos != -1:
    print(f"O array desse numero é: {pos}")
else:
    print("Valor incorrespondente!")