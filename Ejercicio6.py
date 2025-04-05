#Cálculo del índice de masa corporal (IMC)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura * altura)
imc = round(imc, 2)

print("Peso:", peso, "kg")
print("Altura:", altura, "m")
print("IMC:", imc)
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc < 25:
    print("Clasificación: Normal")
elif imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")