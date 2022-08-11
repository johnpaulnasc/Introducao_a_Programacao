salbruto = float(input("Digite o salário bruto: "))


if (salbruto <=420):
    desconto = 0.08
    salliquido = salbruto - (salbruto*desconto)
    print("Com o desconto de oito por cento do INSS, o salário líquido vai ser R$:%.2f" % salliquido)
elif (salbruto > 420 and salbruto <= 1350):
    desconto = 0.09
    salliquido = salbruto - (salbruto*desconto)
    print("Com o desconto de nove por cento do INSS, o salário líquido vai ser R$:%.2f" %salliquido)
else:
    desconto = 0.1
    salliquido = salbruto - (salbruto*desconto)
    print("Com o desconto de dez por cento do INSS, o salário líquido vai ser R$:%.2f" % salliquido)
