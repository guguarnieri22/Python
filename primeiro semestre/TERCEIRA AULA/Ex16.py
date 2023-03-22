h = int(input('Digite o valor da hipotenusa: '))

ca = int(input('Digite o valor do primeiro cateto: '))

co = int(input('Digite o valor do cateto: '))

if (h * h) == (ca * ca) + (co * co):
    print ('É um triangulo retangulo!')

else:
    print('Não é um triangulo retangulo: ')