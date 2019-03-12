
c=0
n=int(input("Por favor, ingrese el número de filas:"))

for i in range (n+1):
    for l in range (0,i):
        z=i+l
        print(end=str(z))
    print(" ")
    i=i+c
    c=c+1