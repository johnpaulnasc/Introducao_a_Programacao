print("1 = Depositar\n2 = Sacar\n3 = Consultar Saldo\n4 = Sair")
valor = int(input("Digite o valor da opção: "))
sac = 0
dep = 0
saldo = 0
dep_pro = 0
sac_pro = 0
while valor !=4:
    if (valor == 1):
        dep = float(input("Qual valor deseja depositar: "))
        saldo = dep + saldo
        dep_pro += dep
    elif (valor == 2):
        sac = float(input("Qual valor deseja sacar: "))
        if (saldo < sac):
            print("Saque inválido")
        else:
            saldo = saldo - sac
            sac_pro += sac
            print("Você sacou %.2f" % sac)      
    elif (valor ==3):
        print("Seu saldo é %.2f" % saldo) 
    print("1 = Depositar\n2 = Sacar\n3 = Consultar Saldo\n4 = Sair")
    valor = int(input("Digite o valor da opção: "))
print("Você depositou %.2f" % dep_pro)
print("Você sacou %.2f" % sac_pro)
print("Saldo final é %.2f" % saldo)



        
