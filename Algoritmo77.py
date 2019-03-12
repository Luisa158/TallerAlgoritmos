
usu="luisa"
con="1234"

for i in range (0,3):
    x = input("Por favor, ingrese el nombre de usuario")
    y = input("Por favor, ingrese la contraseña")
    if usu==x and con==y:
        print("Usuario y contraseña correctos")
    else:
      print("Usuario y contraseña incorrectos")


print("Por favor, vuelva a intentarlo mas tarde")
