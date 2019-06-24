def funcion():
    print("imprime esto")

funcion()



def funcion(nombre, apellido):
    nombre = nombre +" " + apellido
    print(nombre)


def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)
    saludar('Pepe Grillo')  # Imprime: Hola Pepe Grillo


def saludar(nombre, mensaje='Hola'):
    print(mensaje,nombre)


def funcion():
    return "Hola Mundo"
def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)
    print(funcion())

def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print("\nPerdiste!")
    else:
        print("\nGanaste!")