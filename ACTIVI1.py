"""6- Definir una función inversa() que calcule la inversión de una cadena.
 Por ejemplo la cadena "estoy probando" debería devolver
la cadena "odnaborp yotse"""


def funcionInversa():
    palabra = input("chacho ponme una palabra que te la lio al escribirtelo: ")
    palabra = palabra[::-1]
    print(palabra)

funcionInversa()

"""Escriba una función es_bisiesto() que determine si un año determinado es 
un año bisiesto.Un año bisiesto es divisible por 4, 
pero no por 100. También es divisible por 400."""

def funcion_es_bisisieto():
    anio = int(input("ponme un numerito :"))
    if anio > 0:
        if anio % 4 == 0:
            if anio % 100 == 0:
                if anio % 400 == 0:
                    print('chacho lo pusiste bien el año es bisiesto')
                else:
                    print('chacho lo pusiste mal no es bisiesto')
            else:
                print('Hermano que el año es bisiesto.')
        else:
            print('Hermano que  el año no es bisiesto.')
    else:
        print(" no me sea de tu pueblo pon un numero positivo")

funcion_es_bisisieto()

"""Diseñar un sistema de puntos para el juego El reino del dragón:
La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos,
entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. 
Si el jugador pierde, saldrá en pantalla el total de los puntos que realizo y la opción de empezar 
de nuevo.
"""


def puntuacion(puntos, ganado=True):
    if ganado:
        puntos += 100
    else:
        print(puntos)
        empezar_de_nuevo()


"""Ejercicio 1
Determinar la cantidad de dígitos de un numero (1- 100000).
"""
def digitos(n):
    n = int(input("pon me el númerito"))
    if n >1 :
        if n= n/10
            return 1 + digitos(n)
        elif n<=100000:
            return 1
    else:
        return False


digitos(n)



"""
Ejercicio 2 
Para un numero N menor de 100. Mostrar la suma de los cuadrados de los 
números que están separados entre si cuatro posiciones.
Ejercicio 3
Imprimir 10 veces la serie de números de 1 a 10.
Ejercicio 4
Para un número N imprimir su tabla de multiplicar.
Ejercicio 5
Identificar si la suma de los dígitos de un numero es par o impar.
Ejercicio 6
Solicitar un número e imprimir los dígitos pares de este
Ejercicio 7
Los números de las claves de dos cajas fuertes están mezcladas en un número entero llamado clave maestra. Determine ambas claves, la primera clave se construye con los dígitos impares de la clave maestra y la segunda con los pares. Ejemplo: Clave Maestra= 12345, clave1=135, clave2=24.
"""






