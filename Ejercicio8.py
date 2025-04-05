#Conversión de una cantidad en dólares a distintas monedas

dolares = float(input("Ingrese la cantidad en dólares: "))
tasa_euro = 0.92
tasa_libra = 0.79
tasa_yen = 151.5
euros = dolares * tasa_euro
libras = dolares * tasa_libra
yenes = dolares * tasa_yen

print("Cantidad en dólares:", dolares)
print("Equivalente en euros:", euros)
print("Equivalente en libras:", libras)
print("Equivalente en yenes:", yenes)