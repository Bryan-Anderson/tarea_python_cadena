# le pedimos al usuario que escriba una frase
guardar_frase_usuario = input("Escriba una frase:  ")

# le pedimos al usuarion que escriba una vocal
guardar_vocal_usuario = input("Escriba una vocal:  ")

# convertimos la vocal a mayuscula para resaltar
vocal_resaltar_mayuscula = guardar_vocal_usuario.upper()

# imprimos el resultado por pantalla de la frase y de la vocal resaltada
print("La frase escrita con la vocal introducida es: ", guardar_frase_usuario.replace(guardar_vocal_usuario, vocal_resaltar_mayuscula))