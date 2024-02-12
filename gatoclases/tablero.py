from colorama import Fore, Back, Style, Cursor

class Tablero:
    def __init__(self,color_fondo,color_rayas,color_numeros,color_x,Color_y) -> None:
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

        