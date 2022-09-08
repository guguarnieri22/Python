from re import M


a = float(input("Digite a base de seu retangulo: "))

b = float(input("Digite a altura de seu retangulo: "))

m = a * b
print("O tamanho de seu terreno é", m)

if (m >= 100):
    print("Seu terreno é grande")
else:
    print("Seu terreno é pequeno")
