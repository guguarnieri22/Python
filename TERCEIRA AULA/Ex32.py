num = int(input("Digite o primeiro valor: "))

num2 = int(input("Digite o segundo valor: "))

while(num2 < num):
    print("O primeiro valor deve ser menor!")
    num = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

print("Ok, o segundo valor é maior que o primeiro!")
