#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Johana Rangel
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    numero_1= float(input('Ingrese el primer número real: ')) 
    numero_2= float(input('Ingrese el segundo número real: ')) 

    suma= numero_1 + numero_2
    print('La suma entre %.2f y %.2f es %.2f' % (numero_1, numero_2, suma))

    resta= numero_1 - numero_2
    print('La resta entre %.2f y %.2f es %.2f' % (numero_1, numero_2, resta))

    mutiplicacion= numero_1 * numero_2
    print('La multiplicación entre %.2f y %.2f es %.2f' % (numero_1, numero_2, mutiplicacion))

    division= numero_1 / numero_2
    print('La division entre %.2f y %.2f es %.2f' % (numero_1, numero_2, division))

    potencia= numero_1 ** numero_2
    print('La potencia de %.2f y %.2f es %.2f' % (numero_1, numero_2, potencia))


def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''
    nombre_completo= str(input('Ingrese nombre y apellido completo: ')) 
    dni= int(input('Ingrese su numero de DNI: ')) 
    edad= int(input('Ingrese su edad: '))
    altura= float(input('Ingrese su altura en metros, separado por punto: '))

    print('Nombre Completo: %s, DNI: %d' %(nombre_completo, dni))
    print('Nombre Completo: %s, Edad: %d, Altura: %.2f metros' %(nombre_completo, edad, altura))


def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''
    nombre_completoPadre_1= str(input('Ingrese primer nombre y primer apellido del primer padre:'))
    nombrePadre_1, apellidoPadre_1= nombre_completoPadre_1.split(' ')
    
    nombre_completoPadre_2= str(input('Ingrese primer nombre y primer apellido del segundo padre:'))
    nombrePadre_2, apellidoPadre_2= nombre_completoPadre_2.split(' ')
    
    nombre_hijo= str(input('Ingrese nombre del hijo:'))
    print('El nombre completo del hijo es: %s %s %s,' %(nombre_hijo, apellidoPadre_1, apellidoPadre_2))
    


def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    nombreCompleto_persona_1= str(input('Ingrese primer nombre y primer apellido de la persona 1:'))
    nombreLista_persona_1= nombreCompleto_persona_1.split(' ')
   
    nombreCompleto_persona_2= str(input('Ingrese primer nombre y primer apellido de la persona 2:'))
    nomPersona_2, apePersona_2= nombreCompleto_persona_2.split(' ')
    
    esPariente_persona_1= apePersona_2 in nombreLista_persona_1
    print(nombreCompleto_persona_2, 'es pariente de', nombreCompleto_persona_1, esPariente_persona_1)



def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''

    nombreCompleto= str(input('Ingrese su nombe completo:'))
    print(nombreCompleto.lower())
    print(nombreCompleto.upper())
    print(nombreCompleto.capitalize())


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
