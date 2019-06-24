mi_lista =["Juan","Antonio", "Pedro","Herminio"]
for nombre in mi_lista:
    print(nombre)


# como fucniona la palabrata reservada run
for years in range(2001, 2013):
    print("Informes del Año", str(years))




#define la funcion y despues la llamas
def funcion():
    return "Hola Mundo"
frase = funcion()
print(frase)


#sobre los parametrros
def fuccion(nombre, apellido):
    nombre = nombre +" "+ apellido
    print(nombre)


def saludar(nombre, mensaje='Hola'):
   print(mensaje, nombre)
    saludar('Pepe Grillo')  # Imprime: Hola Pepe Grillo

def saludar(nombre, mensaje='Hola'):
    print(mensaje,nombre)

#Llamadas de retorno
def funcion():
    return "Hola Mundo"
def saludar(nombre, mensaje='Hola'):
    print (mensaje, nombre)
    print (funcion())

def jugar(intento=1):
    respuesta = raw_input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print("\nPerdiste!"
    else:
print ("\nGanaste!")

    jugar()