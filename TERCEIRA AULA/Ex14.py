peso = float(input("Digite seu peso: "))

alt = float(input("Digite sua altura: "))

imc = peso / (alt * alt)

if (imc < 20):
    print('Você esta abaixo do peso!')
elif(imc < 25):
    print('Você esta no peso ideal!')
else:
    print('Você esta acima do peso!')