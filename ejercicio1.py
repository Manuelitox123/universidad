"promaga de calcula de cuotas"
gasto_total= 0 ; deuda_pagar=0
amigo1:0 ; amigo2:0; amigo:0
gasto_total = float(input("hola indiqueme cuanto fue el gasto en total de los 3: "))
deuda_pagar = gasto_total / 3
amigo1 = float(input("cuanto gasto el primer amigo "))
amigo2 = float(input("cuanto gasto el segundo amigo "))
amigo3 = float(input("cuanto gasto el tercer amigo "))
deuna1 = deuda_pagar - amigo1
deuna2 = deuda_pagar - amigo2
deuda3 = deuda_pagar - amigo3
print("-------------------------------")
print("primer amigo puso:",amigo1)
print("segundo amigo puso:",amigo2)
print("tercer amigo puso:",amigo3)
print("-----------------------------")
print("primer amigo debe:",deuna1)
print("segundo amigo debe:",deuna2)
print("tercer amigo debe:",deuda3)

