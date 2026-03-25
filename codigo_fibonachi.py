"""este problema da una serie de numeros de la serie de fibonacci. el programa debe preguntar al usuario si desea ingresar otro numero o no. """
suma = 0 ; n2 = 1 ; n3 = 0
while n2 < 100 :
    print(n2)
    suma = suma + n2
    n2 = n2 + n3
    n3 = n2 - n3
print("la suma de los numeros de la serie de fibonacci es: ", suma)