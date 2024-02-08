# Hacer que el usuario pueda ingresar varios datos, que se guarden en una lista y que se haga un sorteo aleatorio de los datos ingresados.
import random as rd

def datos():
    Lista = []
    while True:
        dato = input("Ingrese un dato: ")
        if dato == "":
            break
        else:
            Lista.append(dato)
            
    Lista.sort()
    print(Lista)


if __name__ == "__main__":
    datos()