validacion = "nota invalida"; s ="no"
print("ingrese las notas del estudiante")
while s =="si" :
    n1=int(input("nota numero uno:"))
    if n1 < 0 or n1 > 100:
        print(validacion)
        s ="no"
while s =="si" :           
    n2 = int(input("nota numero dos:"))
    if n2 < 0 or n2 > 100:
        print(validacion)
        s="no"
while s =="si" :
    n3 = int (input("nota numero tres:"))
    if n3 < 0 or n3 > 100:
        print(validacion)
        s="no"
nota1_v= n1 * 0.25
nota2_v= n2 * 0.35
nota3_v= n3 * 0.40
p= (nota1_v + nota2_v + nota3_v) + 3



