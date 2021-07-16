# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
palabra_1 = str(input())    # Miguel

print('Ingrese palabra 2:')
palabra_2 = str(input())    # Angel

print('Ingrese palabra 3:')
palabra_3 = str(input())    # López

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla
palabra_1="Miguel"  # Al darle valores a las variables palabra_1, palabra_2, palabra_2 éstas reemplazan a los valores que entran por consola
palabra_2="Angel"   # Al darle valores a las variables palabra_1, palabra_2, palabra_2 éstas reemplazan a los valores que entran por consola
palabra_3="López"   #Estas tres líneas 26, 27 y 28 deben comentarse o borrarse.
palabra_nueva=(palabra_1[0]+palabra_2[0]+palabra_3[0])
print(palabra_nueva)        # MAL

