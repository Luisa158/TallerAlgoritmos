
print("Bienvenido, este programa te representara las horas, minutos y segundos")

z=int(input("Por favor, ingrese los segundos"))

h=int(z/3600)
m=int((z-(h*3600))/60)
s=z-((h*3600)+(m*60))

print(str(h)+ ":" +str(m)+":" +str(s))




