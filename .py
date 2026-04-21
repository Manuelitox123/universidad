notas =0;nota=0;sw=1;s=""
while sw ==1:
    for i in range(1):
        nom=(input("ingrese su nombre :"))
        notas=0
        for j in range (3):
            nota = int(input("ingrese su nota: "))
            notas+= nota
        print (nom, "tu promedio es: ", notas/3)
    s=input("desea continuar?(S/N): ").upper()
    if s == "N":
        sw =0

