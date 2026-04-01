#declaracionde variables
x=0; y =0 ; z= 0; intentos= 0; famas= 0 ; toques= 0; import random
print ("hola bienvenido al juego de toque y fama")
print("=========================================")
A= random.randint(0, 9)
B= random.randint(0, 9)
C= random.randint(0, 9)
while A == B or A == C : 
    A = random.randint(0, 9)
while B == A or B == C : 
    B = random.randint(0, 9)
while C == A or C == B : 
    C = random.randint(0, 9)
print(A,B,C)

while intentos < 10 and famas < 3 :
    toques =0
    famas =0 
    intentos += 1
    x = int(input("ingrese la primera cifra "))
    y = int(input("ingrese la segunda cifra "))
    z = int(input("ingrese la tercera cifra "))
    print("-------------------")
    # Validacion famas 
    if x == A :
        famas += 1
    if y == B :
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