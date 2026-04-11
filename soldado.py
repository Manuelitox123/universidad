#codigo de soldado caido en terreno enemigo
import random; sw=1; y=0; x=0;z=1
y = int(print("en que columna empieza el soldado: "))
x = int(print("en que fila empieza el soladado: "))
while y <1 or y > 15:
    print ("columna invalida")
    y = int(print("en que columna empieza el soldado: "))
while x <1 or x > 12:
    print("fila invalida.")
    x = int(print("en que fila empieza el soladado: "))
while sw == 1 and z == 1:
    m= random.randint(1,4)
    #movimiento
    if m == 1 and y >1 :#abajo
        y -=1
    elif m == 2 and y <15:#arriba
        y +=1 
    elif m == 3 and x >1: #izquierda
        x -=1
    if x <8:
        if m == 4 and x<15:
            x +=1
    #mina
    ym= random.randint(4,15)
    xm= random.randint(8,12)
    

