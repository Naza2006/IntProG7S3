print("Conversion de segundos a horas, minutos y segundos")
print("-"*60)
cantidad_segundos = int(input("Digite la cantidad de segundos: "))
horas = cantidad_segundos // 3600
print(f"Cantidad de horas: {horas} horas")
multiplicador_horas = horas * 3600
resto_horas = cantidad_segundos - multiplicador_horas
minutos = resto_horas // 60
multiplicador_minutos = minutos * 60
segundos = resto_horas - multiplicador_minutos

print(f"Cantidad de Horas : {horas} horas")
print(f"Cantidad de Minutos : {minutos} minutos")
print(f"Cantidad de Segundos : {segundos} Segundos")
