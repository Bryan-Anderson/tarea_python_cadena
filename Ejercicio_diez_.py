# Primero, pedimos al usuario que introduzca los productos de la cesta de la compra.
productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")
# A continuación, dividimos los productos en una lista.
productos = productos.split(",")
# Por último, mostramos por pantalla cada uno de los productos en una línea distinta.
for producto in productos:
    print(producto)