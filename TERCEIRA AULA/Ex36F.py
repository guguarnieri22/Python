from re import I


num = int(input("Digite um valor: "))

while(num <= 0):
    print("Numero negativo!")
    num = int(input("Digite um valor: "))

a = int(input("Digite o inicio: "))

b = int(input("Digite o fim: "))

while(b <= a):
    print("Errado!")
    b = int(input("Digite o fim: "))
i = 1

for i in range(b, a-1, -1):
    t = num * i
    print(num, 'x', i, '=', t)



