matriz = [[None]*3 for i in range(0,3)]
for i in range(0,2):
    for j in range (0,3):
        matriz[i][j] = int(input("Digite um número: "))

coluna1= 0
coluna2 = 0
coluna3 = 0
cont = 0

for i in range(0,2):
    for j in range(0,3):
        print(matriz[i][j])
    coluna1 += matriz[i][0]
    coluna2 += matriz[i][1]
    coluna3 += matriz[i][2]
print("Soma da primeira coluna: %d" % coluna1)
print("Soma da segunda coluna: %d" % coluna2)
print("Soma da terceira coluna: %d" % coluna3)
                        
