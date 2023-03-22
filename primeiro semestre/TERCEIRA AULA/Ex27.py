print("Se for par soma 5, se for impar soma 8!")
num = int(input('Digite o numero que deseja saber se é par ou impar: '))
div = num % 2


if div == 1:
    print('ÍMPAR!',num + 8)
else:
    print('PAR!',num + 5)
