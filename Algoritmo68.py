
n=int(input("¿Cuántos números desea imprimir?: "))

positivos=0
negativos=0
pares=0
impares=0
multiplos=0

x=int(input("Por favor, digite un número: "))

while x<=n:
    x=int(input("Por favor, digite un número: "))
    if x>0:
        positivos=positivos+1
    if x<0:
        negativos=negativos+1
    if x%2==0:
        pares=pares+1
    if x%2!=0:
        impares=impares+1
    if x%8==0:
        multiplos=multiplos+1
    x=x+1

print("Los números positivos son: ",positivos)
print("Los números negativos son: ",negativos)
print("Los números pares son: ",pares)
print("Los números impares son: ",impares)
print("Los multiplos de ocho son: ",multiplos)