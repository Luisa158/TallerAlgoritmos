
print("Bienvenido a este programa")

x=int(input("Por favor, ingrese un número menor o igual a 100.000: "))

if x<10000 and x>=1000:
    print("Tiene cuatro dígitos")

if x>=10000 and x<=99000:
    print("Tiene cinco dígitos")

if x<1000 and x>=100:
    print("Tiene tres dígitos")

if x<100 and x>=10:
    print("Tiene dos dígitos")

if x<10:
    print("Tiene un dígito")

