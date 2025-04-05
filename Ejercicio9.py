# Cálculo del tiempo total de una película con comerciales

pelicula = int(input("Ingrese cuanto dura la pelicula en minutos: "))
anuncios = int(input("Ingrese la duración de los anuncios: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales: "))
duracion_pausa = int(input("Ingrese la duración de cada pausa comercial: "))
comerciales_durante = cantidad_pausas * duracion_pausa
duracion_total = pelicula + anuncios + comerciales_durante

print("Duración original de la película:", pelicula, "minutos")
print("Duración total de comerciales:", anuncios + comerciales_durante, "minutos")
print("Tiempo total de la pelicula:", duracion_total, "minutos")