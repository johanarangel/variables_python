# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())    # helado

print('Ingrese palabra 2:')
palabra_2 = str(input())    # peldaño

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados
pal_1 = (palabra_1[:3])
pal_2 = (palabra_2[:2])
print(pal_1,pal_2)
pal_nueva = (pal_1 + pal_2)
print(pal_nueva)