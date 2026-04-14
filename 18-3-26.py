"""clase practica del 18-3-26. resolver problemas con while. """
sumu=0; x=1; cont=1
k= int(input("ingrese un numero: "))
while x <= k :
    print (x)
    sumu = sumu + x
    x = x + cont
    cont = cont + 1
print("la suma es:", sumu)
