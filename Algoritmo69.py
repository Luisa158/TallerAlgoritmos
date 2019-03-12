
cont100=0
cont5=0
contleidos=0
while cont5<=80 and cont100<=100:
    a=int(input("valor deseado: "))
    contleidos+=1
    if a%2==0:
        cont100+=1
    if a==5:
        cont5+=1

print("la cantidad de valores leidos es: ",contleidos)
print("con una cantidad de pares: ",cont100)
print("con un cantidad de 5 de: ", cont5)