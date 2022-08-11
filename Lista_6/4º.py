matriz = [[None]*3 for i in range(0,3)]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input("Digite um número: "))
        
aux1 = matriz[0][1]
matriz[0][1] = matriz[1][0]
matriz[1][0] = aux1
aux2 = matriz[1][2]
matriz[1][2] = matriz[2][1]
matriz[2][1] = aux2

for i in range(0, 3):
    for j in range(0, 3):
        print(matriz[i][j])
        
