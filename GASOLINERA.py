#venda de gasolina por optanage y litros
a = 1299; b = 1405; c = 1615 ; tp = 0; ltotales=0;montot=0; s=0
while s == 0:
        op = input("hola indique que tibpo de octaje va a comprar A/B/C (93/95/97): ").upper()
        forma= input("que tipo de compra va hacer por litros(L)o por monto(M):").upper()
        #forma de pagar por monto
        if forma =="M":
            m = int(input("ingrese el monto que desea cargar: "))
            if op == "A":
                ltotales= m/a
            elif op == "B":
                ltotales= m/b
            elif op == "C":
                ltotales= m/c
            montot += m
        #forma de pagar por litros
        elif forma == "L":
            l = int(input(("ingrse la cantidad de liros que llevara: ")))
            if op == "A":
                tp = l*a
            elif op == "B":
                tp= b*l
            elif op == "C":
                tp = c*l
            montot+= tp
    #resultados del programa
        if forma == "L":
            print ("##############################################")
            print ("Este es le monto a pagar:",tp,"por",l,"litros")
        elif forma == " M":
            print("estos son los litros totales que llevara:", ltotales, "por", m)
        print("esta es la plata que llevas hasta ahora:", montot)
        print("este es optanaje mas vendido: ")
    #continuar ?
        s = input("continuar?(SI/NO) : ").upper()
        if s == "NO" :
            S = 1