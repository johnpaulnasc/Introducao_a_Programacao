game_of_thrones = True
ruim = 0
reg = 0
bom = 0
exc = 0
idbom = 0
idvelha = 0
cont = 0
vezes = 0
while game_of_thrones == True:
    idade = int(input("Informe a idade: "))
    print("1 = Ruim\n2 = Regular\n3 = Bom\n4 = Excelente")
    nota = int(input("Qual a sua nota: "))
    if (nota == 1 ):
        ruim += 1   
    elif (nota == 2):
        reg += 1
    elif (nota == 3):
        idbom = idbom + idade
        bom += 1
    elif (idade > 40 and nota == 4):
        exc += 1
    elif (idade > idvelha):
        idvelha = idade
    print("1 = Sim\n2 = Não")
    continuar = int(input("Quer continuar?"))
    if (continuar == 2):
        game_of_thrones = False
print("A quantidade de pessoas que deram como respota ruim foi %d" % ruim)
print("A quantidade de pessoas que deram como resposta regular foi %d" % reg)
print("A quantidade de pessoas acima de 30 anos que respoderam excelente foi %d" %exc)
print("A quandidade de pessoas mais velha de 30 anos que respoderam  %d anos" %idvelha)
            
            
    
        
    

        
