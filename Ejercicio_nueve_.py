# Este programa pregunta al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Primero, pedimos al usuario que introduzca la fecha de su nacimiento.
fecha_de_nacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
# A continuación, dividimos la fecha de nacimiento en tres partes: día, mes y año.
dia, mes, año = fecha_de_nacimiento.split("/")
# Por último, mostramos por pantalla el día, el mes y el año.
print("Día:", dia)
print("Mes:", mes)
print("Año:", año)