palavra = input("Digite a palavra codificada: ").split(' ')
caracteres = ('', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
for i in range(len(palavra)):
    m = int(palavra[i])+1-1
    print(caracteres[m],end='')
    
