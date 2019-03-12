
print("Bienvenido a este  programa")

x=int(input("Por favor, ingrese el valor de la venta"))

c=x*19/100
b=x+c

print("El valor de la venta es " +str(x), "Elvalor del IVA es "+str(c), "El valor con IVA incluido es" +str(b))

if x>150000:
 z=b*5/100
 d=b-z
 print("El valo total es" +str(d))
