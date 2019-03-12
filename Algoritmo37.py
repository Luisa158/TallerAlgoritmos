
print("Bienvenido, est programa te dira el valor del pasaje")

a=float(input("Por favor, ingrese la distancia en km: "))
b=float(input("Por favor, ingrese los días que se va a quedar"))

p=5000
pd=a*p
vd=(pd*b)*15/100

if vd>1000:
    print("Se hara un descuento " +str(vd))

if pd<100000:
    print("El precio del pasaje es " +str(pd))
