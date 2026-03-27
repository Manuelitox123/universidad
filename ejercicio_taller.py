print("indique la temperatura en grados celcius. ")
t = int(input("temperatura (c°): "))
if t < 0 :
    print("Bajo cero ")
elif t > 0 and t <= 14 :
    print("frio")
elif t >= 15 and t <= 24:
    print ("Templado")
elif t >= 25 and t <= 34 :
    print("calido")
else:
    print("muy caliente")