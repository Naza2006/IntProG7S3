#Cálculo del precio final de un producto con impuestos y descuentos

precio = float(input("Ingrese el precio original del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
descuento_aplicado = (precio * descuento) / 100
precio_descuento = precio - descuento_aplicado
iva = float(input("Ingrese el porcentaje de IVA: "))
iva_calculado = (precio_descuento * iva) / 100
precio_final = precio_descuento + iva_calculado

print("Precio original:", precio)
print("Descuento aplicado:", descuento_aplicado)
print("Precio con descuento:", precio_descuento)
print("IVA calculado:", iva_calculado)
print("Precio final:", precio_final)