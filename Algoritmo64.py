
suma = 0
prom=0
n=int(input("¿Cuántos números desea calcular?: "))

for i in range (1,n+1,1):
    x=int(input("Por favor, ingrese un número: "))
    suma = suma+x
print("La suma es: ",suma)

prom=suma/n
print("El promedio es: ", prom)