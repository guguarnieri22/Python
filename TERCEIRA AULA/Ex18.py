a = float(input("Digite o valor da aceleração (em m/s2): "))

b = float(input("Digite o valor da velocidade inicial (em m/2): "))

temp = float(input("Digite o valor do tempo de percurso (t em s): "))

v = b + (a * temp)

if (v <=40):
    print("Veiculo esta lento, a velocidade é", v)
elif (v <=60):
    print("Velocidade permitida, a velocidade permitida é", v)
elif (v <= 80):
    print("Velocidade de cruzeiro, a velocidade permitida é:", v)
elif (v <= 120):
    print("Veiculo muito rapido, a velocidade é:", v)
else:
    print ("Veiculo muito rapido, a velocidade é: ", v)