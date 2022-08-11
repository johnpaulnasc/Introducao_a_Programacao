num = int(input("Digite um valor: "))
cont = 0

while num > 0:
    if num > 0:
        num = num // 10
        cont += 1
    else:
        cont == 1
print("Possui %d algorismo" % cont)
