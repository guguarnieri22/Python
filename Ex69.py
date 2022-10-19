matriz = [ [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],]

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = int(input('Digite um numero: '))
            
        
 
mult = int(input("Digite um multiplicador: "))

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = matriz [l][c] * mult



for i in range(0, 3, 1):
    print(matriz[i])

 
