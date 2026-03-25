cantidad_acumulada = 0
precio_total_acumulado = 0
descuento_total = 0
producto_con_descuento = 0
segur= "si"
while segur != "no" and segur != "NO":
    print("hola aqui se calcula el precio + iva")
    precio_neto = int(input("ingrese el precio del producto: "))
    cantidad = int(input("ingrese la cantidad del producto: "))
    precio_total = precio_neto * cantidad
    iva = precio_total * 0.19
    precio_final = precio_total + iva
    if cantidad > 2 :
        descuento = precio_final * 0.10
        precio_final = precio_final - descuento
        producto_con_descuento = producto_con_descuento + cantidad
        descuento_total = descuento_total + descuento
        print("descuento aplicado: ", descuento)
    print("el precio final es:", precio_final)
    print()
    print("gracias por su compra")
    segur = input("desea calcular otro precio? si/no: ")
    precio_total_acumulado = precio_total_acumulado + precio_final
    cantidad_acumulada = cantidad_acumulada + cantidad
if segur == "no" or segur == "NO":
    print()
    print("precio total de compras: ", precio_total_acumulado)
    print("cantidad de productos comprados: ", cantidad_acumulada)
    print("productos con descuento: ", producto_con_descuento)
    print("descuento total: ", descuento_total)
    print()
    print("gracias por usar el programa")