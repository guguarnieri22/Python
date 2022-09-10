from time import sleep


p1 = int(input("Digite o primeiro valor: "))
p2 = int(input("Digite o primeiro valor: "))
p3 = int(input("Digite o primeiro valor: "))
p4 = int(input("Digite o primeiro valor: "))
p5 = int(input("Digite o primeiro valor: "))
p6 = int(input("Digite o primeiro valor: "))
p7 = int(input("Digite o primeiro valor: "))
p8 = int(input("Digite o primeiro valor: "))
p9 = int(input("Digite o primeiro valor: "))
p10 = int(input("Digite o primeiro valor: "))

def maior(*num):
    cont = maior = 0
    print ("Analizando...")
    for valor in num:
        print (f"{valor}", end= '', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}")