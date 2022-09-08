from re import I


num = int(input("Digite um numero positivo para exibir a sua tabuada: "))

while(num <= 0):
    print("Insira um numero positivo!")
    num = int(input("Digite um numero positivo para exibir a sua tabuada: "))

i = 1

while(i < 11):
    r = num * i
    print(f'{num} * {i} = {r}')
    i = i + 1
