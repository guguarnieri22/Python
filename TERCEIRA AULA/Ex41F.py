s = int(input("Digite o valor da sequencia que deseja visualizar: "))

a = 2
b = 5

r = a + b

while(a > 100):
    print("Digite o valor novamente: ")
    a = int(input("Digite um valor menor que 100: "))

for i in range(3, s, 2):
    print(r)
    a = b
    b = a
    a = r
    r = a + b

