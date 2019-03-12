

print(" PARES E IMPARES")
x = int(input("¿Cuántos valores va a introducir? "))
if x < 0:
    print("¡Imposible!")
else:
    pares = 0
    for i in range(1, x + 1):
        numero = int(input(f"Escriba el valor {i}: "))
        if numero % 2 == 0:
            pares += 1
    print(f"Ha escrito {pares} números pares y {x - pares} números impares")
impares=x-pares
promedioPares=pares/x
promedioImpares=impares/x
print("El promedio de los pares es: ",promedioPares)
print("El promedio de los impares es: ",promedioImpares)