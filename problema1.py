suma = 0 ; x= 1
k= int(input("ingrese un impar que sera el tope de la serie: "))
print("la serie es: ")
while x < k:
    print(x)
    suma = suma + x
    x = x + 2
print("la suma de la serie es: ", suma)
