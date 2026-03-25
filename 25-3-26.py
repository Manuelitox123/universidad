#programa para buscar el numero de personas y sus edades
#asignacion de variables
m = 0; h=0; cont=0; edad_mayor = 0; edad_menor =5000 ; nombre_mayor = ""; nombre_menor = ""
t = int(input("hola indique la cantidad de personas total: "))
while cont < t:
    print("-----------------------------------------------")
    nombre = (input ("cual es el nombre de la personas: "))
    sexo =input ("cual es el sexo de la persona (m/f): ")
    edad = int(input("cual es la edad de la persona: "))
    if sexo== "m" or sexo == "M":
        h += 1
    elif sexo == "f" or sexo == "F":
        m += 1
    if edad >= edad_mayor:
        edad_mayor = edad
        nombre_mayor= nombre
    if edad <= edad_menor:
        edad_menor = edad
        nombre_menor = nombre
    cont += 1
print("----------------------------------")
print ("numeor de hombres: ", h )
print ("numero de mujeres: ", m)
print ("la edad mayor es: ", edad_mayor, "es:", nombre_mayor)
print ("la edad menor es: ", edad_menor, "es", nombre_menor)
print (nombre)