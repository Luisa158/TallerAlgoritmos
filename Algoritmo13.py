
print("Bienvenido al intercambio de variables")

x=int(input("Por favor, ingrese el primer valor"))
y=int(input("Por favor, ingrese el segundo valor"))

print("Las variables originales son ", (x,y))

c=x
x=y
y=c

print("Las variables en el intercambio son ", (x,y))