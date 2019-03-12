
print("Se pedira el peso de cada de sus bultos, si no lleva por favor escribir 0")

cont1=0
cont2=0
bultos=0
pesoTotal=0
valorTotal=0

for i in range(0,30):
    a=int(input("Siguiente bulto"))
    if i==0:
        cont1=a
        cont2=a

    if a<cont2 and a!=0:
        cont2=a

    if a>cont1 and  a<501:
        cont1=a

    if a!=0 and a>0 and a<25:
        bultos+=1
        pesoTotal=pesoTotal+a

    if a!=0 and a>25 and a<300:
        bultos+=1
        pesoTotal=pesoTotal+a
        valorTotal=valorTotal+(a*1500)

    if a!=0 and a>300 and a<=500:
        bultos += 1
        pesoTotal = pesoTotal + a
        valorTotal = valorTotal + (a*2500)

    if a>500:
        print("Este bulto no sera puesto en el avión por exceso de peso")

    if a==0:
        break

    if pesoTotal>1800:
        print("No podemos subir esto al avión, porque su peso es: ",pesoTotal,"el peso debe ser menor o igual a 1800 y este sobrepasa")

    else:
        if pesoTotal<1800:
            print("El número total de bultos es: ",bultos)
            print("El peso del bulto mas pesado es: ",cont1, "\nEl bulto menos pesado es: ",cont2)
            print("El promedio de peso por bulto es: ",(pesoTotal/bultos))
            print("El precio total de bultos es: ",valorTotal)
            print("El precio en dolares seria: ",(valorTotal*3165)) #el valor del dolar del día sábado
            print("El peso de los bultos es: ",pesoTotal)

