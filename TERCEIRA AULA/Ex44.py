qtde = 10
soma = 0

while(num <= 0):
    num = int(input("Esse numero é negativo, digite novamente: "))
for i in range(1, 11, 1):
    num = int(input("Digite um numero: "))

    if(i == 1):
        maior = num
    elif (num > maior):
        maior = num

    # soma
    soma = soma + num

#media
media = soma / 10

print("O maior é:", maior)
print("A soma é:", soma)
print("A media é:", media)