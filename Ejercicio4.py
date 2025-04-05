#Cálculo del tiempo total de un viaje con escalas

tramo1 = float(input("Duración del primer tramo del vuelo (en horas): "))
escala1 = float(input("Duración de la primera escala (en horas): "))
tramo2 = float(input("Duración del segundo tramo del vuelo (en horas): "))
escala2 = float(input("Duración de la segunda escala (en horas): "))
tramo3 = float(input("Duración del tercer tramo del vuelo (en horas): "))
tiempo_total = tramo1 + escala1 + tramo2 + escala2 + tramo3

print("Tiempo total del viaje:", tiempo_total, "horas")