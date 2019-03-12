
print("Bienvenido a este programa")

a=float(input("Por favor, ingrese el primer número"))
b=float(input("Por favor, ingrese el segundo número"))
c=float(input("Por favor, ingrese el tercer número"))

if(a > b and a > c):
 x=a
else:
 if(b > a and b > c):
  x=b
 else:
   x=c
if(a < b and a < c):
 y=a
else:
 if(b < a and b < c):
  y=b
 else:
  y=c

print("el mayor es "+str(x)+" y el menor es "+str(y))

