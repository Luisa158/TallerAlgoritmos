
x=""

n=int(input("Por favor, ingree el número de filas: \n"))
for i in range(1,n+1):
    for w in range (1,i+1):
     x=x+"@"
    x=x+"\n"

print(x)