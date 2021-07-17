# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo
print(nombre, apellido)

# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo = nombre + apellido

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
cantidad_letras = len(nombre_completo) 
print(len(cantidad_letras)) #Esto te da un error que dice "Object of type int has no len()", esto significa 
                            #que la variable cantidad_letras es el número de carácteres que tiene el nombre completo
                            #y si vuelves a usar len(cantidad_letras) alli salta el error porque la función len() es para string no enteros int
