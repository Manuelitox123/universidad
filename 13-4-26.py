#progrmna de los robots 
energiap= 500;energiao=500;import random; ty =0; tx=0;oliviay=15;oliviax=1;popeyey=15;popeyex=10;metay=1;metax=1;sw=1;sv=1;choque=0;sr=0
tr = 0
print("en este progrma dos robots comperitan por llegar a la meta y tu colocaras una trampa" \
"en algun lugar del mapa")
ty= int(input("coloque en que fila esta la trampa: "))
tx=int(input("coloque en que columna esta la trampa: "))
while sv ==1:
#verificacion de trampa
    while ty < 1 or ty >15:
        print ("solo puedes poner filas entre el 1 y el 15.")
        ty= int(input("coloque en que fila esta la trampa: "))
    while tx < 1 or tx>10:
        print("solo puedes poner columnas entre 1 y 10.")
        tx=int(input("coloque en que columna esta la trampa: "))
    while ty==15 and tx ==1 or ty==15 and tx ==10:
        print("en ese lugar hay un robot no pudes poner una mina ahi.")
        ty= int(input("coloque en que fila esta la trampa: "))
        tx=int(input("coloque en que columna esta la trampa: "))
    if ty!=15 or tx !=10:
        tr +=1
    if ty!=15 or tx !=1:
        tr +=1
    if ty >=1 and ty<=15:
        sr+=1
    if tx >=1 and tx<=10:
        sr +=1
    if sr == 2 and tr==2:
        sv=2
while sw ==1:
#moviemto olivia
    if energiao > 0:
        direc= random.randint(1,4)
        if direc == 1 and oliviay >1 :#arriba
            oliviay -= 1
            energiao -=5
        elif direc == 2 and oliviay <15 :#abajo
            oliviay+=1
            energiao -=5
        elif direc == 3 and oliviax > 1: #izquierda
            oliviax -=1
            energiao -=5
        elif direc == 4 and oliviax < 10 :#derecha
            oliviax +=1
            energiao -=5
    print ("olivia se movio a: (", oliviax,oliviay,") le queda", energiao,"de energia")
    if oliviax == tx and oliviay == ty:
        print( "olivia cayo en la trampa ")
#moviento popeye
    if energiap > 0:
        popeyex = random.randint (1,10)
        popeyey = random.randint (1,15)
        energiap -=5
    print ("popeye se movio a: (",popeyex,popeyey,") le queda", energiap,"de energia")
    if popeyex == tx and popeyey == ty:
        print( "popeye cayo en la trampa ")
#trampa
    if popeyex == tx and popeyey == ty:
        energiap -=10
    if oliviax == tx and oliviay ==ty:
        energiao -=10
#meta 
    if popeyex == metax and popeyey == metay:
        sw = 2
    if oliviax == metax and oliviay == metay:
        sw = 3
#sin bateria 
    if energiao == 0 and energiap ==0 :
        sw =5
#choque entre robots
    if popeyex == oliviax and popeyey == oliviay:
        choque +=1
print("##################################################")
print("los resultados fueron: ")
print ("olivia quedo en la posision: (",oliviax,oliviay,")")
if energiao ==0 :
    print("olivia se quedo sin bateria ")
if sw== 3:
    print ("felizidades olivia gano la carrera")
print("popeye quedo en la pocicion: (",popeyex,popeyey,")")
if energiap ==0 :
    print("popeye se quedo sin bateria ")
if sw== 2:
    print ("felizidades popeye gano la carrera")
if choque > 1:
    print ("se chocaron :",choque,"veses")
