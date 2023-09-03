# Pedir al usuario que ingrese su correo electrónico
correo_usuario = input("Por favor, escriba su correo electrónico: ")

# Dividir el correo electrónico en nombre de usuario y dominio
nombre_correo_usuario, dominio = correo_usuario.split("@")

# Crear el nuevo correo electrónico con el dominio "ceu.es"
nuevo_correo = nombre_correo_usuario + "@ceu.es"

# Mostrar el nuevo correo electrónico por pantalla
print("Su nuevo correo electrónico es:", nuevo_correo)
