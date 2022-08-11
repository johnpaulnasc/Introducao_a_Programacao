pessoas = 0
while True :
    idade = int(input("Digite sua idade: "))
    if (idade <0):
        break
    altura = float(input("Digite sua altura: "))
    if (idade >= 18 and altura >= 1.70):
        pessoas = pessoas + 1
print("%d pessoas são acima de 18 anos e 1,70 de altura" % pessoas)
        
        
        
        
        
        
