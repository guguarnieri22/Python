num = int(input("Insira um numero positivo para exibir a sua tabuada: "))

while(num <= 0):
    print("Insira um numero positivo!")
    num = int(input("Insira um numero positivo para exibir a sua tabuada: "))
i = 1
for i in range(1, 11, 1):
    r = num * i
    print(f'{num} * {i} = {r}')
    i = i + 1
