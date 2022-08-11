var1 = int(input("Digite o primeiro valor:"))
var2 = int(input("Digite o segundo valor:"))

aux = var1
var1 = var2
var2 = aux

print("Os valores do primeiro e segundo após a troca:%d e %d" % (var1,var2))
