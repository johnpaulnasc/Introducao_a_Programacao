valor = float(input("Digite o valor:"))
formaP = input("Forma de pagamento(dinheiro,cheque ou cartão):")

if((formaP == "dinheiro" and valor >= 100) or (formaP == "Dinheiro" and valor >=100)):
    desconto = valor - (valor*0.1)
    print("O valor com desconto foi de: %.2f" % desconto)
elif((formaP == "Cheque") or (formaP == "cheque")):
    print("Não houve desconto.")  
elif((formaP == "Cartao") or (formaP == "cartao") or (formaP == "Cartão") or (formaP == "cartão")):
    cartao = input("Débito ou crédito:") 
    if((cartao == "Debito") or (cartao == "debito") or (cartao == "Débito") or (cartao == "débito")):
        print("Ficará o valor inicial e sem desconto.")      
    elif((cartao == "Credito") or (cartao == "credito") or (cartao == "Crédito") or (cartao == "crédito")):
        parcelas = int(input("Quantas parcelas:"))
        if(parcelas == 1):
            cartaocre = valor/1
            print("Ficará 1 vezes de %.2f" % cartaocre)
        elif(parcelas == 2):
            cartaocre = valor/2
            print("Ficará 2 vezes de %.2f" % cartaocre)              
        elif(parcelas == 3):
            cartaocre = valor/3
            print("Ficará 3 vezes de %.2f" % cartaocre)              
        else:
            print("Quantidade de parcelas inválidas")
