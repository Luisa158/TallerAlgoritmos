
print("Bienvenido a este programa")

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

if notafinal<2.0:
 print("No puede habilitar")

if notafinal<3.0:
    print("Ha reprobado la asignatura")

if notafinal>=3.0:
    print("Aprobo la asignatura")

if notafinal>4.5:
    print("Felicitaciones por tu calificación alta")

