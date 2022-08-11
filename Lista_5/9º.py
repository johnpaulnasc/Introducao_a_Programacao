num = int(input("Digite um valor:"))
num1=0
num2=1
for i in range (1,num):
    seq = num2
    num2 = num2 + num1
    num1 = seq
    print(seq)
print("Sequência de Fibonacci %d" % num2)
