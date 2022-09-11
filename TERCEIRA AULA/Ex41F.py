n = int(input("Digite um valor menor que 100: "))
while(n<=0 and n>100):
    print("Erro!")
    n = int(input("Digite um valor menor que 100: "))

for i in range(3,n+1,2):
    if(i == 0):
        a = ((i+1)*(i+1))+1
        print(a)
