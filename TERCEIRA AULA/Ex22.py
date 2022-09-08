menu = input("Selecione uma opção das seguintes: \n 1- Triangulo \n 2- Retangulo \n 3- Quadrado \n 4- Circulo \n -:")


if (menu == "1"):
    b = float(input("Digite a base de seu triangulo: "))
    a = float(input("Digite a altura de seu triangulo: "))

    res = (b * a) / 2

    print("A área do seu triangulo é:", res)

elif (menu == "2"):
    a = float(input("Digite o primeiro lado de seu retangulo: "))
    b = float(input("Digite o segundo lado de seu retangulo: "))

    c = a * b

    print("A base de seu retangulo é:", c)

elif (menu == "3"):
    a = float(input("Digite um dos lados do seu quadrado: "))

    b = a * a

    print("A base de seu quadrado é:", b)

elif (menu == "4"):
    c = float(input("Digite o raio do seu circulo: "))

    a = c * 3.14
    print("A área de seu circulo é", a)
else:
    print("Digite uma alternativa válida!")