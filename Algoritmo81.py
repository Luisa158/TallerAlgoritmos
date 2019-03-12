


n=int(input("Por favor, ingree el número de filas: \n"))
for i in range(n):
    x=''
    for w in range (n):

     if w>=i:
         x+='* '
     else:
         x+=' '

    print(x)