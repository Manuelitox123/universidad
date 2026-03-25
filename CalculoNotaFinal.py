# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:38:11 2026

@author: Dagoberto Cabrera
"""

Nombre = input("Ingrese nombre : ")
Nota1 = float(input("Nota 1 = "))
Nota2 = float(input("Nota 2 = "))
Nota3 = float(input("Nota 3 = "))

NotaFinal = 0.25*Nota1 + 0.35*Nota2 + 0.4*Nota3
print()
print("El estudiante ", Nombre, " obtuvo ", NotaFinal)

if NotaFinal >= 4 :
    print("APROBADO")
    print("FELICITACIONES")
else :
    print("REPROBADO")
    print("LO SIENTO")
input()

