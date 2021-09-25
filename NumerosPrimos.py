cont = 0

x = input("Ingrese Numero"+ " ")
num = int(x)

for i in range(num + 1):
    for j in range(1, i + 1):
        if i % j == 0:
           cont=cont+1
    if cont == 2:
        print(i)
    cont = 0
        



