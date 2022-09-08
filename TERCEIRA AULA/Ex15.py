a = float(input('Digite o primeiro lado de seu triangulo: '))

b = float(input('Digite o segundo lado de seu triangulo: '))

c = float(input('Digite o terceiro lado de seu triangulo: '))

if ( ( ( a + b ) > c ) and ( ( a + c ) > b ) and ( ( b + c ) > a) ):
    if ( (a==b) and (b==c) ):
        print("Tringulo equilatero!")
    elif ( (a!=b) and (a!=c) and (b!=c) ):
        print("Triangulo isoceles")
    else:
        print("Triangulo escaleno!")
else:
    print("Não é um triangulo!")