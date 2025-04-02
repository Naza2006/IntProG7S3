#Calculo del salario neto

salbru=float(input("Ingrese el salario bruto del empleado: "))
imprenta=salbru*0.1
segurosoc=salbru*0.05
fondopen=salbru*0.03
desctotl=(imprenta+segurosoc+fondopen)
slnet=salbru-desctotl
print("El salario bruto es: ", salbru)
print("El descuento total es: ", desctotl)
print("El salario neto es: ", slnet)