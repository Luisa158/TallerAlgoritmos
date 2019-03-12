
import math

print("Bienvenido, este programa te dira la distancia entre coordenadas")

x1=float(input("Por favor, ingrese la primer coordenada del eje x"))
y1=float(input("Por favor, ingrese la primer coordenada del eje y"))
x2=float(input("Por favor, ingrese la segunda coordenada del eje x"))
y2=float(input("Por favor, ingrese la segunda coordenada del eje y"))


distancia=math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("La distancia es " +str(distancia))
