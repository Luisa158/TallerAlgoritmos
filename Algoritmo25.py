
print("Bienvenido, programa inversa")

a=int(input("Por favor, ingrese un número de cuatro cifras: "))

c1=a%10
c2=int ((a%100)/10)
c3=int((a%1000)/100)
c4=int((a-(a%1000))/1000)

print(str(c1)+str(c2)+str(c3)+str(c4))






