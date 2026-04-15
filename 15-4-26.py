import random;sw=0;intentos=0
ns=random.randint(1,20)
if ns >=1 and ns<=10:
    z="B"
elif ns >=11 and ns <=20:
    z="A"
print("este juego tienes que adivinar en que zona esta  el numero secreto y cual es:")
uz=input("en que zona puerde estar el numero(A/B): ").upper()
while uz != "A" and uz !="B":
    print("###########################################################")
    uz=input("esa zona no esta disponible solo hay una zona (A/B): ").upper()
if uz == z :
    sw =1
if uz != z :
    sw =2
while sw==1:
    print("#############################################")
    un= int(input("coloque un numero para adivinar "))
    if un > ns:
        print("el numero secreto es menor ")
    if un < ns:
        print("el numero es mayor.")
    if ns == un:
        sw =3
    intentos+=1
    if intentos ==4:
        sw = 4
print("##########################################################")
if sw ==2:
    print("usted no acerto la zona a perdido.")
    print("la zona era: ", z)
if sw ==3:
    print("felizidades usted a ganado el numero secreto era:",ns)
    print("el numero de intentos fueron:",intentos)
if sw ==4:
    print ("usted perdio porque ya no tiene intentos ")
    print("el numero secreto era:",ns)