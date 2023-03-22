n=int(input("Digite um valor positivo menor que 100: "))
while(n<=0 or n>100):
    print("Valor invalido!")
    n=int(input("Digite um valor positivo menor que 100: "))

for i in range(0,n,1):
    if(i==0):
        a=((i+1)*(i+1))+1
    else:
        a=a+((i+1)*(i+1))+1
        print(f"O {i+1}º valor é:",a)