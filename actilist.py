""" Ejercicio 1
Escriba una función que tome una lista de números y devuelva la suma acumulada,
es decir, una nueva lista donde el primer elemento es el mismo,
el segundo elemento es la suma del primero con el segundo,
el tercer elemento es la suma del resultado anterior con el
siguiente elemento y así sucesivamente. Por ejemplo,
la suma acumulada de [1,2,3] es [1, 3, 6]."""


def conlista():
    lista = [1,2,3,4,5,6]
    suma = []
    x = 0
    max = len(lista)-1
    while x < max:
        suma[x] = lista[x] + lista[x-1]
        x = x + 1
        print(suma)











