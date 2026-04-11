#programa para jugar con el computados adivinando un numero random 
import random;n = random.randint(1,25);intentos= 0; usuario=0
print("hola bienvenido al juego adivina el numero.") 
while usuario != n:
    usuario= int(input("ingrse el el numero: "))
    while usuario < 1 or usuario > 25:
        usuario= int(input("numero no valido ingrese un numero que este estre 1 y 25: "))
    if usuario - n < -3 :
        print ("el numero es mucho mayor.")
    elif usuario - n <= 3 and usuario != n:
        print ("esta cerquita")
    elif usuario - n > 3 :
        print(" es numero es mucho menor.")
    intentos +=1
#resultados
print ("########################################")
print ("usted a adivinado el numero felicidades.")
print("numero de intentos: ",intentos)