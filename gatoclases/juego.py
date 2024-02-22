from colorama import Cursor
from jugador import Jugador
from tablero import Tablero
import os

class Juego:
    def __init__(self, tablero:Tablero,
                 jugador_a:Jugador,
                 jugador_b:Jugador) -> None:
        self.tablero = tablero
        self.jugador_a= jugador_a
        self.jugador_b= jugador_b
        self.turnos = 0
    
    def ganador(self,jugador:Jugador):
        print(Cursor.POS(10,12)+" "*50)
        print(Cursor.POS(10,13)+f"El ganador es: {jugador.nombre}")
        print(Cursor.POS(10,14)+" "*50)
        print(Cursor.POS(0,15)+"Estadísticas:")
        print(Cursor.POS(0,16)+Jugador.__str__(self.jugador_a))
        print(Cursor.POS(0,17)+Jugador.__str__(self.jugador_b))
        print("")
        self.jugar_otra_vez()
    
    def empate(self):
        print(Cursor.POS(10,12)+" "*50)
        print(Cursor.POS(10,13)+"El juego quedo en empate")
        print(Cursor.POS(10,14)+" "*50)
        print(Cursor.POS(0,16)+"Estadísticas:")
        print(Cursor.POS(0,17)+Jugador.__str__(self.jugador_a))
        print(Cursor.POS(0,18)+Jugador.__str__(self.jugador_b))
        print("")
        self.jugar_otra_vez()

    def jugar(self,moviendo:Jugador,en_espera:Jugador):
        ganador = False
        mov = False
        while mov == False:
            print(Cursor.POS(10,14)+f"Mueve:{moviendo.nombre}")
            mov = self.tablero.juega_usuario(moviendo)
        self.tablero.display()
        if self.tablero.revisa_linea_ganadora():
            self.tablero.display()
            moviendo.juegos["ganados"] += 1
            en_espera.juegos["perdidos"] += 1
            ganador = True
            self.ganador(moviendo)
        else:
            if self.turnos == 8:
                moviendo.juegos["empatados"] += 1
                en_espera.juegos["empatados"] += 1
                self.empate()

        print(Cursor.POS(10,14)+" "*50)
        self.turnos +=1
        return ganador
    
    
    def jugar_otra_vez(self):
        jugar_otra = input("Jugar otra vez? [Y/N]: ").upper()
        if jugar_otra == "Y":
            os.system("clear")
            self.tablero.reset_tablero()
            self.turnos = 0
            self.inicia_juego()
        else:
            print("Juego terminado")

    def inicia_juego(self):
        self.tablero.reset_tablero()
        mov = False
        while self.turnos < 9:
            self.tablero.display()
            g = self.jugar(moviendo=self.jugador_a, en_espera=self.jugador_b)
            if (g != True):
                g = self.jugar(moviendo=self.jugador_b,en_espera=self.jugador_a)
                if (g == True):
                    self.turnos = 9
            else:
                self.turnos = 9
        print("")
        

if __name__ == "__main__":
    lista = ["X","O"]
    a = Jugador("Bob","X",lista)
    b = Jugador("Pat","O",lista)
    tab = Tablero()
    juego = Juego(tab,a,b)
    juego.inicia_juego()
    
        