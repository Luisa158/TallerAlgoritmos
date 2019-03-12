
print("Año bisiesto")

agno=int(input("Introduzca un año: "))
print(agno)

if agno%4==0 or agno%400==0:
    print("Es bisiesto")

elif agno%100==0 and agno%400!=0:
    print("No es bisiesto")