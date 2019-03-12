
print("Secuencia positivo-negativo")

x=int(input("¿Cuántos números quiere imprimir?"))
cont=1

while cont<=x:
    if cont%2==0:
        negativo=cont*-1
        print(negativo)
    else:
        print(cont)
    cont=cont+1