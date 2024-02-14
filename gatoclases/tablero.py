from colorama import Fore, Back, Style, Cursor
from jugador import Jugador

class Tablero:
    def __init__(self,color_fondo=Back.WHITE,color_rayas=Fore.LIGHTCYAN_EX,color_numeros=Fore.BLUE,color_x=Fore.RED,Color_y=Fore.GREEN) -> None:
        self.lista_numeros = [x for x in range(0,9)]
        self.dicc_posiciones = {x:str(x) for x in self.lista_numeros}
        self.combos_ganadores = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.color_fondo = {"rayas":color_rayas,"Fondo":color_fondo,"numeros":color_numeros,"X":color_x,"O":Color_y}
        
        
    def display_tablero(self):
        tablero = self.dicc_posiciones
        reset = Style.RESET_ALL
        bg = self.color_fondo["Fondo"] #Back.white
        blue = self.color_fondo["numeros"] #Fore.BLUE
        board_color = self.color_fondo["rayas"] #Fore.LIGHTCYAN_EX
        x_color = self.color_fondo["X"] #Fore.YELLOW
        o_color = self.color_fondo["O"] #Fore.RED
        X = x_color + "X"
        O = o_color + "O"
        BD = board_color + (" - " * 5)
        BS = board_color + " | "
        d = {}
        for k,v in tablero.items():
            if v == "X":
                d[k] = X + BS
            elif v == "O":
                d[k] = O + BS
            else:
                d[k] = blue + str(k) + BS
        print(Cursor.POS(10, 5)+f"{bg}{"-"}{" "+BD}{" "}{reset}")
        print(Cursor.POS(10, 6)+f"{bg}{"|"}{" "}{" "+d[ 0 ]}{" "}{d[1]}{" "}{d[2]}{" "}{reset}")
        print(Cursor.POS(10, 7)+f"{bg}{"-"}{" "+BD}{" "}{reset}")
        print(Cursor.POS(10, 8)+f"{bg}{"|"}{" "}{" "+d[3]}{" "}{d[4]}{" "}{d[5]}{" "}{reset}")
        print(Cursor.POS(10, 9)+f"{bg}{"-"}{" "+BD}{" "}{reset}")
        print(Cursor.POS(10, 10)+f"{bg}{"|"}{" "}{" "+d[6]}{" "}{d[7]}{" "}{d[8]}{" "}{reset}")
        print(Cursor.POS(10, 11)+f"{bg}{"-"}{" "+BD}{" "}{reset}")
        print(Style.RESET_ALL)
    
    def reset_tablero(self):
                self.dicc_posiciones = {x:str(x) for x in self.lista_numeros}
                
    def revisa_linea_ganadora(self):
        tab = self.dicc_posiciones
        lista_lineas = self.combos_ganadores
        for cmb in lista_lineas:
            if tab[cmb[0]]==tab[cmb[1]]==tab[cmb[2]]:
                return True
            return False
        
    def juega_usuario(self,tab,jugador:Jugador):
        tab = self.dicc_posiciones #tablero
        turno_correcto = False
        usuario = input(Cursor.POS(10,14)+"Escoja celda:")
        usuario = int(usuario)
        if usuario in tab:
            if tab[usuario] == str(usuario):
                tab[usuario]=jugador.simbolo
                turno_correcto = True
            else:
                print(f"Posición {usuario} ocupada")
                print("Eliga otra opción")
        return turno_correcto

if __name__ == "__main__":
    t = Tablero()
    t.display_tablero()
    #t.dicc_posiciones[0] = "X"
    #t.dicc_posiciones[1] = "X"
    #t.dicc_posiciones[2] = "X"
    t.display_tablero()
    #print(f"Gana:{t.revisa_linea_ganadora()}")
    t.reset_tablero()
    lista_simbolos = ['X','O']
    A = Jugador("Bob","X",lista_simbolos)

    while not t.revisa_linea_ganadora():
        t.display_tablero()
        t.juega_usuario(t.dicc_posiciones,A)
        print(f"Gana:{t.revisa_linea_ganadora()}")
        
    t.display_tablero()
    
    