# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:06:01 2026

@author: Dagoberto Cabrera
"""
Cont = 0
Seguir = "S"
while  Seguir == "S" :
    Nombre = input("Ingrese nombre del alumno: ")
    Nota = float(input("INgrese nota de presentación: "))
    if  Nota >= 6 : 
        print("Alumno ", Nombre, " ya está aprobado")
    else : 
        if Nota < 3 : 
            print("Alumno ", Nombre, " ya está REPROBADO")
        else : 
            print("Alumno ", Nombre, " DEBE DAR EXAMEN")
            Cont = Cont + 1
    Seguir = input("¿Más alumnos ? (S/N): ")   
print("Cantida de alumnos que deben dar examen = ", Cont)
print("FIN DEL PROCESO")
input()
 
