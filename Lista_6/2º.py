n = int(input("Quantos valores você deseja inserir: "))
lista = [None]*n
for i in range (0,n):
    lista[i] = int(input("Digite um número: "))
    if (lista[i] % 2 == 0):
        lista[i] *=2
    else:
        lista[i] *=3
print(lista)
        
    
    
    
