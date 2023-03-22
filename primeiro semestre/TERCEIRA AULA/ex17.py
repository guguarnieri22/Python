sex = input('Digite seu sexo(m/f): ')

p = float(input('Digite o seu peso: '))

a = float(input('Digita a sua altura: '))


imc = p / (a * a)


if (sex == 'm'):
    if (imc < 20):
        print(f'Vc esta abaixo do peso!{imc:.2f}')
    elif (imc < 25):
        print(f"Vc esta no peso ideal!{imc:.2f}")
    else:
        print(f"Vc esta acima do peso!{imc:.2f}")


else:
    if (imc < 19):
        print(f"Vc esta abaixo do peso!{imc:.2f}")
    elif (imc < 24):
        print(f"Vc esta no peso ideal!{imc:.2f}")
    else:
        print(f"Vc esta acima do peso!{imc:.2f}")
input()
