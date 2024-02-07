from colorama import Fore, Back, Style, Cursor
tablero = [x for x in range(0,9)] #0,1,2,3...8
tab_dict= {x:str(x) for x in tablero}

def display_tablero(tablero:dict):
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

def juega_usuario(tab):
    turno_correcto = False
    usuario = input("Escoja celda:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            tab[usuario]="X"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto


def juega_usuario1(tab):
    turno_correcto = False
    usuario = input("Escoja celda Jugador/a 1:")
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
    usuario = input("Escoja celda Jugador/a 2:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            tab[usuario]="O"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
            return turno_correcto

def display_score(s:dict,d:dict):
    if d['ganador'] != '':
        print(f"Ganó la partida:{d['ganador']}")
        s[ d['ganador'] ] +=1
    else:
        s['Empates'] +=1
        print("¡El juego quedo en empate!")
    print(f"<<Jugador/a:{s['Jugador/a']}>> <<Computadora:{s['Computadora']}>> <<Empates:{s['Empates']}>>")

def display_score2(s:dict,d:dict):
    if d['ganador'] != '':
        print(f"Ganó la partida: {d['ganador']}")
        s[ d['ganador'] ] +=1
    else:
        s['Empates'] +=1
        print("¡El juego quedo en empate!")
    print(f"<<Jugador/a 1:{s['Jugador/a 1']}>> <<Jugador/a 2:{s['Jugador/a 2']}>> <<Empates:{s['Empates']}>>")
   

if __name__ == "__main__":
    display_tablero(tab_dict)
    juega_usuario(tab_dict)