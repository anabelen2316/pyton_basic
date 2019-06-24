#tamaño 6 mim y 12 max
def comprobarNombre(nombre):

    if (6<=len(nombre)<=12):
       if nombre.isalnum():
           return True
    elif(len(nombre)<6):
        return "El nombre de usuario debe contener al menos 6 caracteres"
    if (not nombre.isalnum()):
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return "El nombre de usuario no puede contener más de 12 caracteres"

