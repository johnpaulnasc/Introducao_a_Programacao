valor = float(input("Digite o valor:"))
formaP = input("Forma de pagamento(dinheiro,cheque ou cartão):")


if (formaP == "dinheiro" and valor >= 100 or formaP == "Dinheiro" and valor >=100):
    desconto = valor - (valor*0.1)
    print("O desconto foi de: %.2f" % desconto)
elif (formaP == "Cheque" or formaP == "cheque"):
    print("Não houve desconto")
else:
    print("Forma de pagamento inválida")
