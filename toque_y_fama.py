#declaracionde variables
s =0 ; x=0; y =0 ; z= 0; intentos= 0; famas= 0 ; toques= 0
print ("hola biemenido al juego de toque y fama")
print("=========================================")
A = int(input("el primer participante inglrese la primera cifra del numeo secreto: "))
B = int(input("el primer participante inglrese la segunda cifra del numeo secreto:"))
C = int(input("el primer participante inglrese la ultima cifra del numeo secreto:"))
while s < 15 :
    print("|")
    s += 1
while intentos < 9 and famas < 3 :
    toques =0
    famas =0 
    intentos += 1
    x = int(input("ingrese la primera cifra "))
    y = int(input("ingrese la segunda cifra "))
    z = int(input("ingrese la tercera cifra "))
    print("-------------------")
    # validacion famas 
    if x == A:
        famas += 1
    if  y == B :
        famas += 1
    if z == C:
        famas +=1
    #validacion toques x
    if x == B or x == C:
        toques +=1
    #validacion toques Y
    if y == A or y == C:
        toques +=1
    #validacion toques z
    if z == A or z == B:
        toques +=1
    print("x  y  z famas y toques")
    print("=======================")
    print(x, "",y,"",z,"-",  famas,"------",  toques)
    print("--------------------------")
    print("intentos: ", intentos)
    pt