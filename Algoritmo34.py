
print("Bienvenido a este programa")

a=float(input("Por favor, ingrese el primer número"))
b=float(input("Por favor, ingrese el segundo número"))
c=float(input("Por favor, ingrese el tercer número"))

if(a > b and a > c):
 print("El numero mayor es " + str(a))
else:
 if(b > a and b > c):
  print("El numero mayor es " + str(b))
 else:
  print("El numero mayor es " + str(c))




