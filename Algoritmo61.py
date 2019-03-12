
print("Números naturales contenidos en otros")

cont=0

x=int(input("Por favor, ingreese el primer número: "))
y=int(input("Por favor, ingrese un número mayor al anterior: "))

if x>y:
 print("El segundo número debe ser mayor que el primero")

else:
    while x<=y:
        print("Número natural: ",x)
        x=x+1