"""promedio de edad y cantidad de personas."""
s= "SI" ; mujeres = 0 ; hombres = 0 ; edad_mujeres = 0 ; edad_hombres = 0 ; cantidad = 0 ; menores = 0 ; mayores = 0 
promedio_hombres=0; promedio_mujeres=0
while s != "NO":
    print("------------------------------------------------------------")
    nommbre = input ("ingrese el nombre de la personas: ")
    genero = input ("ingrese el genero de laa persona F/M: ").upper()
    edad = int(input("ingrese la edad de la persona: "))
    while edad < 0 or edad >120:
        print("edad no disponible")
        edad = int(input("ingresa una edad entre 0 y 120: "))
    cantidad += 1
    "gurdado de menores y mayores"
    if edad < 18 :
        menores += 1
    else :
        mayores += 1
    "guardado de edades por mujeres y hombres"
    if genero == "M": 
        edad_hombres = edad_hombres + edad
        hombres += 1 
    elif genero == "F":
        edad_mujeres = edad_mujeres + edad
        mujeres += 1
    print()
    s = input ("desea continuar si/no: ").upper()
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
