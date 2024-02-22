import os
from juego import Juego
from jugador import Jugador
from tablero import Tablero

def main():
    lista = ['X','O']
    jugador1 = input("Nombre del jugador 1: ")
    jugador2 = input("Nombre del jugador 2: ")
    print("")
    
    if jugador1 == jugador2:
        print("Los nombres de los jugadores no pueden ser iguales")
        jugador2 = jugador1 + "2"
        print(f"Jugador 2 se llamará {jugador2}")
        print("")
        
    simbolo1 = input(f"{jugador1} escoja un símbolo entre {lista}: ").upper()
    if simbolo1 not in lista:
        simbolo1 = lista.pop()
        print(f"El símbolo escrito no está disponible. Simbolo '{simbolo1}' asignado a {jugador1}.")
    if simbolo1 in lista:
        lista.remove(simbolo1)
    simbolo2 = lista.pop()
    print("")
    print(f"El símbolo de {jugador1} es '{simbolo1}'")
    print(f"El símbolo de {jugador2} es '{simbolo2}'")
    print("")
    
    lista = [simbolo1,simbolo2]
    a = Jugador(jugador1,simbolo1,lista)
    b = Jugador(jugador2,simbolo2,lista)
    tab = Tablero()
    juego = Juego(tab,a,b)
    empezar = input("Empezar el juego? [Y/N]: ").upper()
    if empezar == "Y":
        os.system("clear")
        juego.inicia_juego()
    else:
        print("Juego cancelado")
    
    
    
    
if __name__ == "__main__":
    main()