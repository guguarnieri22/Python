primeiro = int(input("Digite o primeiro valor: "))

segundo = int(input("Digite o segundo valor: "))

terceiro = int(input("Digite o terceiro valor: "))

if(primeiro > segundo and terceiro):
    print ("O primeiro valor e maior!")
elif segundo > primeiro and terceiro:
    print("Segundo valor e o maior!")
else:
    print("O terceiro valor e o maior!")