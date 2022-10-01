numeros = []

for i in range (0, 21, 1):
    numeros.append(int(input("insira o num: ")))

m = int(input("Digite a constante: "))

for i in range(0, 20, 1):
    numeros[i] = numeros[i] * m

for i in numeros:
    print(i)


