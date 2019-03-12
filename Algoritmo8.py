
print("Bienvenido, este programa te dira tu nota final")

n1=float(input("Por favor, ingrese la primer nota"))
n2=float(input("Por favor, ingrese la segunda nota"))
n3=float(input("Por favor, ingrese la tercera nota"))
n4=float(input("Por favor, ingrese la cuarta nota"))
n5=float(input("Por favor, ingrese la quinta nota"))

a=n1*15/100
b=n2*20/100
c=n3*15/100
d=n4*30/100
e=n5*20/100

notafinal=(a+b+c+d+e)

print("La nota final es ",(notafinal))
