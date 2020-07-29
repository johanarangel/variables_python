#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Johana Rangel
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Johana RAngel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    #print('Valores decimales ingresados son, primer: ', numero_1, ' y segundo: ', numero_2)
    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    suma= numero_1 + numero_2
    print('El resultado de sumar %.2f y %.2f es %.2f' % (numero_1, numero_2, suma)) 

    Resta= numero_1 - numero_2
    print('El resultado de restar %.2f y %.2f es %.2f' % (numero_1, numero_2, Resta))

    Division= numero_1/numero_2
    print('El resultado de dividir %.2f y %.2f es %.2f' % (numero_1, numero_2, Division))

    Multiplicacion= numero_1*numero_2
    print('El resultado de multiplicar %.2f y %.2f es %.2f' % (numero_1, numero_2, Multiplicacion))

def ej2():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    print(nombre, apellido)
    # Almacenar su nombre completo en una variable
    # nombre_completo = .....
    nombre_completo= nombre + apellido
    # Imprimir la cantidad de letras que posee su nombre completo
    print(len(nombre_completo))

def ej3():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla.
    
    acronimo= palabra_1[0] + palabra_2[0] + palabra_3[0]
    print('%s, %s, %s, %s' % (palabra_1, palabra_2, palabra_3, acronimo))

def ej4():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    primeras_letras= palabra_1[:3]
    print(primeras_letras)
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    ultimas_letras=palabra_2[-3:]
    print(ultimas_letras)
    
    # Formar una nueva palabra con los recortes solicitados
    nueva_palabra= primeras_letras + ultimas_letras
    
    # Imprima en pantalla los resultados
    print(nueva_palabra)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
