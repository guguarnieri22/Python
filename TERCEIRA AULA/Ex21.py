valor1 = float(input("Digite o primeiro valor: "))

valor2 = float(input("Digite o segundo valor: "))

print("MENU")

menu = input("Selecione uma das segintes: \n m - multiplicação \n d - divisão \n a - adição \n s - subtração \n Digite uma das opções a cima: ")


if (menu == "m"):
    r = valor1 * valor2
    print("Seu valor é : ", r)

elif (menu == "d"):
    r = valor1 / valor2
    print("Seu valor é : ", r)

elif (menu == "a"):
    r = valor1 + valor2
    print("Seu valor é : ", r)

elif (menu == "s"):
    r = valor1 - valor2
    print("Seu valor é : ", r)


else:
    print('Valor não corresponde a nenhuma alternativa anteriores')