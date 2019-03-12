
cont1=0
cont2=0
cont3=0
cont4=0

a=float(input("¿cuántos números quiere leer?"))

while cont1<a:
    a = float(input("Por favor, ingrese un número"))
    cont1+=1

    if cont1<100:
        cont2+=1
    if cont1>100:
        cont3+=1
    if cont1==100:
        cont4+=1
print("Los números mayores a 100 son: ",cont3,"\nLos menores a 100 son: ",cont2,"\nLos iguales  100 son: ",cont4)