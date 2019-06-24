from io import open
#crear fichero y escribir dentro
texto = "Una lineas con texto\nOtra lineas con textos\nOtras lineas mas abajo del tido"
fichero = open("fichero.txt","w",encoding ="utf8")# fichero.txt ruta donde lo crearemos, w indica modo de escritura, write (puntero principio)
fichero.write(texto)# Escribimos dentro del fichero el contenido de la variable texto
fichero.close()#Cuando dejamos de trabajar, cerramos el fichero siempre

#lectura de un fichero de texto
fichero = open("fichero.txt", "r", encoding="utf8")
texto = fichero.read()  # Escribimos dentro del fichero el contenido de la variable texto
fichero.close()#Cuando dejamos de trabajar, cerramos el fichero siempre
print(texto)

#se almacena las lineas del fichero
fichero = open("fichero.txt","r",encoding ="utf8")
lineas = fichero.readlines()
fichero.close()
print(lineas)
print(lineas[-1])

#fichero inexistentes
fichero = open("fichero_inventado.txt","r",encoding ="utf8")
| = fichero.readline() #linea a linea
|
"una linea con texto\n"
| = fichero.readline()
|
""


