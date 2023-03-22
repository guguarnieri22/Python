valor = float(input("Insira o valor pago na mercadoria:"))

menu = input("Selecione a forma de pagamento: \n 1- À vista em dinheiro ou cheque, recebe 10 porcento de desconto \n 2- À vista no cartão de crédito, recebe 15porcento de desconto \n 3- Em duas vezes sem juros \n 4- Em quatro vezes, preço normal de etiqueta mais juros de 10 porcento \n -:")


if (menu == "1"):
    
    pag = valor -(0.1 * valor)
    print("O valor a ser pago é", pag)

elif(menu == "2"):

    pag =valor -(0.15 * valor)
    print("O valor a ser pago é", pag)

elif(menu == "3"):

    pag = (valor / 2) 
    print("O valor a ser pago é duas vezes de", pag)

elif(menu == "4"):

    pagam = valor +(0.1 * valor)
    par = pagam / 4
    print("O valor a ser pago é 4 vezes de", par)

else:
    print("Insira uma opção valida!")