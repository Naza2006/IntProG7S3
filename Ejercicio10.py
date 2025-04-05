#Cálculo del volumen de un cilindro y su área superficial

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
pi = 3.1416
area_base = pi * (radio ** 2)
volumen = area_base * altura
area_lateral = 2 * pi * radio * altura
area_superficial = area_lateral + 2 * area_base

print("Radio ingresado:", radio)
print("Altura ingresada:", altura)
print("Volumen del cilindro:", volumen)
print("Área superficial del cilindro:", area_superficial)