from colorama import Fore, Back, Style, Cursor

def display_tablero(tablero: dict):
    reset = Style.RESET_ALL
    bg = Back.BLACK
    blue = Fore.BLUE
    board_color = Fore.WHITE
    x_color = Fore.YELLOW
    o_color = Fore.RED
    X = x_color + "X"
    O = o_color + "O"
    BD = board_color + (" - " * 5)
    BS = board_color + " | "
    d = {}
    for k, v in tablero.items():
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
    
def juega_usuario1(tab):
    turno_correcto = False
    usuario = input(Cursor.POS(0,13) + "Escoja celda:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            tab[usuario]="X"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto  

def juega_usuario2(tab):
    turno_correcto = False
    usuario = input(Cursor.POS(0,13) + "Escoja celda:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            tab[usuario]="O"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto
         
         
if __name__ == "__main__":
    display_tablero({0:'X',1:'O',2:'X',3:'O',4:'X',5:'O',6:'X',7:'O',8:'X'})