# Conversión de temperatura

fah = float(input("Ingresa la temperatura en grados Fahrenheit: "))
cel = (fah - 32) * 5 / 9
kel = cel + 273.15

print("Temperatura en Celsius:", cel)
print("Temperatura en Kelvin:", kel)