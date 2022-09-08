a = float(input("Digite seu peso: "))

b = float(input("Digite sua altura: "))

m =b / (a * a) 

if m < 20:
    print("Vc esta magrinho cara!")
elif m < 25:
    print("Ta no peso correto!")
else:
    print("Precisa parar com McDonals!")
