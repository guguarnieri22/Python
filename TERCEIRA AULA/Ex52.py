numeros = []

for i in range(0, 11, 1):
    num = int(input('Digite um valor: '))
    numeros.append(num)

m = numeros[0]

for i in range(0, 10, 1):    
    if (numeros[i] > m):
            m = numeros[i]

print('Maior numero é ', m)