"""promedio de edad y cantidad de personas."""
s= "si" ; mujeres = 0 ; hombres = 0 ; edad_mujeres = 0 ; edad_hombres = 0 ; cantidad = 0 ; menores = 0 ; mayores = 0 
promedio_hombres=0; promedio_mujeres=0
while s== "si":
    print("------------------------------------------------------------")
    nommbre = input ("ingrese el nombre de la personas: ")
    genero = input ("ingrese ewl genero de laa persona f/m: ")
    edad = int(input("ingrese la edad de la persona: "))
    cantidad += 1
    "gurdado de menores y mayores"
    if edad < 18 :
        menores += 1
    else :
        mayores += 1
    "guardado de edades por mujeres y hombres"
    if genero == "m" or genero == "M" :
        edad_hombres = edad_hombres + edad
        hombres += 1 
    elif genero == "f" or genero == "F" :
        edad_mujeres = edad_mujeres + edad
        mujeres += 1
    print()
    s = input ("desea continuar si/no: ")
"promedios"
promedio_general= (edad_hombres+edad_mujeres) / cantidad
if edad_hombres > 0 :
    promedio_hombres= edad_hombres / hombres
if edad_mujeres > 0: 
    promedio_mujeres= edad_mujeres / mujeres
print ()
print("los resultados son:")
print()
print("son en total: ", cantidad )
print("las mujeres totales son: ", mujeres)
print("la cantidad de  hombres son: ", hombres)
print("la cantidad de menores es:", menores)
print("la cantidad de  mayores es: ", mayores)
print("el promedio general de edades es: ", promedio_general)
print("el promedio de edad en mujeres es: ", promedio_mujeres)
print("el promedio de edad de los hombres es:", promedio_hombres)
