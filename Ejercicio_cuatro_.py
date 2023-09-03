
# Primero, pedimos al usuario que introduzca un número de teléfono.
numero_de_telefono = input("Introduce un número de teléfono con el formato prefijo-número-extension: ")
# A continuación, comprobamos si el número de teléfono introducido tiene el formato correcto.
if not numero_de_telefono.startswith("+34-"):
    print("El número de teléfono introducido no tiene el formato correcto.")
    exit()
# Si el número de teléfono tiene el formato correcto, lo dividimos en tres partes: prefijo, número y extensión.
prefijo, numero, extension = numero_de_telefono.split("-")
# Por último, mostramos por pantalla el número de teléfono sin el prefijo y la extensión.
print("El número de teléfono sin el prefijo y la extensión es:", numero)