
def namemen():

    nombres_masculinos = ["Alvaro", "Jacinto", "Miguel", "Edgardo", "David"]

    nombres_masculinos.append("Jose")#añade elementos
    print(nombres_masculinos)

    nombres_masculinos.extend(["Jose", "Gerardo"]) #
    print(nombres_masculinos)

    nombres_masculinos.insert(0, "Ricky") #en la posion o0 añade el elemnto señalado
    print(nombres_masculinos)

    nombres_masculinos.pop() #elimina un elemntos ultimo de la lista
    print(nombres_masculinos)

    nombres_masculinos.pop(3) #elimina el que esta en la posion 3
    print(nombres_masculinos)

    nombres_masculinos.remove("Jose")#añade elemtnos por su valor
    print(nombres_masculinos)

    nombres_masculinos =["Alvaro", "Miguel", "Edgardo", "David", "Miguel"]
    nombres_masculinos.count("Miguel") #busca el elemento



    nombres_masculinos = ["Alvaro", "Miguel", "Edgardo", "David", "Miguel"]
    nombres_masculinos.count("Miguel")

    nombres_masculinos.sort()#ordena la lista en orden reverso
    print(nombres_masculinos)

    nombres_masculinos.sort(reverse=True)#odenar una lista de forma decente
    print(nombres_masculinos)

    nombres_masculinos =["Alvaro", "Miguel", "Edgardo", "David", "Miguel"] #te cuenta cuantas veces hay dos lementoas de la lista
    nombres_masculinos.count("Miguel")

    nombres_masculinos = ("Alvaro", "Miguel", "Edgardo", "David", "Miguel")
    nombres_masculinos.count("Miguel")

    nombres_masculinos.index("Miguel") #contar la cantidad de apariciones elemntos
    nombres_masculinos.index("Miguel",2,5) #obtener numerpo de indice

    tupla = (1,2,3,4,)#conversion de tupla a listas y a la inversa
    tupla

    lista = [1,2,3,4]
    lista

    tupla(lista)

    #concatenacion siemple de colecciones
    lista1 = [1, 2, 3, 4]
    lista2 = [3, 4, 5, 6, 7, 8]
    lista3 = lista1 + lista2
    lista3

    tupla1 = (1, 2, 3, 4, 5)
    tupla2 = (4, 6, 8, 10)
    tupla3 = (3, 5, 7, 9)
    tupla4 = tupla1 + tupla2 + tupla3
    tupla4

    #valor maximo y minimo
    max(tupla4)
    max(tupla1)
    mim(tupla1)
    min(lista3)
    mim(lista1)

    #contar elementos
    len(lista3)
    len(lista1)
    len(tupla2)

namemen()

    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry") #llega Terry
    queue.append("Graham") #llega Graham
    queue.popleft() #el primero en llegar ahora se va



    def estedicionaros(): #esta funcion copia un diccionario
        dicionarios = {"color": "violeta", "talle": "XS", "precio": 174.25}
        remera = dicionarios.copy()
        dicionarios
        ramera
        dicionarios.clear()
        dicionarios
        remera
        musculosa = remera
        remera
        musculosa
        remera.clear()
        remera
        musculosa

    #crear un nuevo dicionario desde las claves de una secuencias
    def secun():
        secuencias = ["color", "talle", "marca"]
        diccionario = dict.fromkeys(secuencia)
        diccionario
        dicionario2 = dict.fromkeys(secuencia, 'valor x defecto')
        dicionario2

     #concatenar diccionarios
        diccionario = {"color": "verde", "precio": 45}
        dicionario2 = {"talle": "M", "marca": "Lacoste"}
        diccionario.update(dicionario2)
        diccionario

    #establacer una clave y valor por defecto
    def esta_valor()
        ramera = {"color": "rosa", "marca": "Zara"}
        clave = ramera.setdefault("talle", "U")
        clave
        ramera1 = ramera.copy()
        ramera2
        clave = ramera2.setdefault("estampado")
        clave
        ramaera2
        clave = ramera2.setdefault("marca","Lacoste")
        clave
        ramera2

        #Obtener el valor de una clave
        remera.get("color")
        remera.get("stock")
        remera.get("stock", "sin stock")

        #Saber si una clave existe en el diccionario
        existe = remera.in("precio")
        existe
        existe = remera.in("color")
        existe

        #Obtener las claves y valores de un diccionario
        diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
        #iteritemps--> ahora es items
        for clave, valor in diccionario.items():
        print ("El valor de la clave"+ clave," es " "valor")