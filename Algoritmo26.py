
print("Programa expresiones")

x=True
y=False

a=x or y
b=y or y
c=x and x
d=y and x
e=(y and y) or (x and x)
f=(y or y) and (x and x)

print("El resultado de la condición True or False es: ",a)
print("El resultado de la condición False or False es: ",b)
print("El resultado de la condición True and True es: ",c)
print("El resultado de la condición False and True es:  ",d)
print("El resultado de la condición (False and False) or (True and True) es: ",e)
print("El resultado de la condición (False or False) and (True and True) es: ",f)