valor = 0
soma = 0
valor = int(input("Digite o valor: "))
maior_valor = valor
menor_valor = valor
while valor != -1:
    if (valor>maior_valor):
        maior_valor = valor
    elif (menor_valor < maior_valor and valor < menor_valor):
        menor_valor = valor    
    soma = valor + soma
    valor = int(input("Digite o valor: "))
print("Maior valor é %d" % maior_valor)
print("Menor valor é %d" % menor_valor)
print("Soma dos valores %d" % soma)
        
        
