p1 = float(input("Digite a primeira nota: "))

p2 = float(input("Digite a segunda nota: "))

res = (p1 + 2 * p2) / 3

if (res > 5):
    print(f"Sua nota é {res:.2f} e você esta aprovado!")
else:
    print(f"Sua nota foi {res:.2f} e você esta reprovado!")