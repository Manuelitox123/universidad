"""
solucion al problema 2 del taller 1 de programacion
1,2,4,7,11,16,22,29,37,46
"""
suma = 0 ; x= 1 ; cont= 1
k = int(input("ingrese un numero el cual sera el final de la serie: "))
print("la serie es: ")
while x <= k:
    print(x)
    suma = suma + x
    x = x + cont
    cont = cont + 1
print("la suma de la serie es: ", suma)

