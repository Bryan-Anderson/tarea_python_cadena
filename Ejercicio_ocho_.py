# Este programa pregunta por consola el precio de un producto en quetzales con dos decimales y muestra por pantalla el número de quetzales y el número de centavos del precio introducido.
precio = float(input("Introduce el precio del producto en quetzales: "))
if precio < 0:
    print("El precio introducido no es válido.")
    exit()
quetzales = int(precio)
centavos = int((precio - quetzales) * 100)
print("El precio del producto es de", quetzales, "quetzales y", centavos, "centavos.")