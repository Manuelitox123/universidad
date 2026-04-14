""" clase practica del 18-3-26 problema numero 2. hacer un programa de calcule el promedio de edad de un grupo de personas. 
el programa debe preguntar al usuario si desea ingresar otra edad o no. """
n = 0 ; s = 0 ; edad = 0 ; menor = 0
cantidad = int(input("ingrese el numero de personas: "))
while n < cantidad :
    print()
    nombre= input("ingrese el nombre de la persona: ")
    edad = int(input("ingrese la edad de la persona: "))
    s = s + edad
    n = n + 1
    print("la edad de ", nombre, " es: ", edad)
    if edad < 18 :
        menor = menor + 1
promedio = s / cantidad
print()
print("cantidad de personas menores de edad: ", menor)
print("el promedio de edad del grupo es: ", promedio)

