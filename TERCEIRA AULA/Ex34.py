print('Tabuada do 5 com for!')
 
num = int(input("Digite o numero 5, para obter a sua tabuada: "))
 
while(num != 5):
    print("Insira o numero 5!")
    num = int(input("Digite o numero 5, para obter a sua tabuada: "))
 
for i in range(1, 11, 1):
    r = num * i
    print(f'{num} X {i} = {r}')