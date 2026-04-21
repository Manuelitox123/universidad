#codigo de soldado caido en terreno enemigo
import random; sw=1; y=0; x=0;muralla=1;tiempo=0;mt=0;tiempomuralla=0; pared = 0
y = int(input("en que fila empieza el soldado: "))
x = int(input("en que columna empieza el soladado: "))
#verificacion
while y <1 or y > 15:
    print ("fila invalida")
    y = int(input("en que fila empieza el soldado: "))
while x <1 or x > 8:
    print("columna invalida.")
    x = int(input("en que columna empieza el soladado: "))
#while del movivento 
print("############################################")
while sw == 1:
#movimiento
    m= random.randint(1,4)
    if m == 1 and y >1 :#abajo
        y -=1
        tiempo +=1
    elif m == 2 and y <15:#arriba
        y +=1 
        tiempo +=1
    elif m == 3 and x >muralla: #izquierda
        x -=1
        tiempo +=1
    if m== 4 and x<12:
        x +=1
        tiempo +=1
    print("el soldado se movio a la pocicion (",x,y,") minuto", tiempo)
#muralla
    if x >7 and pared == 0 : 
        pared = 1
        muralla=8
        mt= tiempo
#mina
    ym= random.randint(4,15)
    xm= random.randint(8,12)
    if ym == y and xm==x:
        sw = 2
#zona de salvacion 
    if y < 4 and x > 8:
        sw =3 
print("########################################################")
if sw ==3:
    print("el soldado se a salbado")
    print("el soldado duro", tiempo,"minutos")
    print("la muralla se levanto en el minuto:", mt)
if sw == 2:
    print("el sondado murio por una mina ")
    print("la muralla se levanto en el minuto:", mt)



