num = int(input("Digite um valor para exibir a tabuada: "))

while(num <= 0):
    print("Numero negativo, digite novamente.")
    num = int(input("Digite um valor para exibir a tabuada: "))

a = int(input("Digite o inicio da sequencia: "))

b = int(input("Digite o final da sequencia: "))

while(b <= a):
    print("Errado. O inicio deve ser maior!")
    b = int(input("Digite o final da sequencia novamente: "))
i = 1

while(b <= a):
    t = num * b
    print(num, 'x', b, '=', t)
    b = b - 1
