#programa de un robot moviendose en un plano cartesiano, el robot se mueve a la derecha, izquierda, arriba o abajo dependiendo de la letra que ingrese el usuario. el programa debe preguntar al usuario si desea ingresar otro movimiento o no. al final se debe mostrar la posicion final del robot.
y= 1; x=1;s = 1; import random; b=30;sec=0
print("el robot comienza en coordenadas ", x, y)
print("-----------------------------------------")
while s == 1 :
    # direccion del robot, 1=arriba , 2= derecha, 3=abajo, 4= izquirda
    direc= random.randint(1,4)
    if direc == 1 and y < 9:
        y += 1
        b-= 1
    elif direc == 2 and x < 9:
        b-= 1
        x +=1
    elif direc == 3 and y > 1:
        b-= 1
        y -= 1
    elif direc == 4 and x>1 :
        b-= 1
        x-=1
    print("el robortavanso a","(x",x,",y",y,")", "energia",b)
    #break
    if x==5 and y== 5 :
        s = 0
    if b == 0 :
        s = 0
    #recarga de bateria
    if x == 1 and y == 1 :
        b=30
    elif x == 9 and y == 9 :
        b=30
    elif x == 1 and y == 9 :
        b=30
    elif x == 9 and y == 1 :
        b=30
    sec +=1
#resultados del programa
print("---------------------------------------")
if b == 0:
    print("el robot se a quedado sin energia")
if x == 5 and y == 5 :
    print ("elrobot a cadido en el agujero se a destruido" )
    print("quedo con ",b,"de bateria")
print ("queodo en la posicion (",x,y,")")
print("el robot duro ", sec, "segundos caminado")
print("----------------------------------------")

