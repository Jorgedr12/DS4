'''
Lógica del programa del gato
'''
import random
import board

tablero = [x for x in range(0,9)] #0,1,2,3...8
tab_dict= {x:str(x) for x in tablero}
tab_dict = {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8"}

def display_tablero(tab:dict):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("-----------")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("-----------")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")

def ia(board:dict):
    ocuppied = True
    while ocuppied == True:
        r = random.choice(list(board.keys()))
        if board[r] == str(r): # Si está libre
            board[r] = "O"
            ocuppied = False
            
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

def check_winner(tab,lista_lineas):
    for cmb in lista_lineas:
        if tab[cmb[0]]==tab[cmb[1]]==tab[cmb[2]]:
            return True
    return False

def combinacion_ganadora(tab,lista_lineas):
    for cmb in lista_lineas:
        if tab[cmb[0]]==tab[cmb[1]]==tab[cmb[2]]:
            print(f"La combinación ganadora es {cmb}")
            return cmb
    return False

def game(tab:dict):
    diccionario = {'ganador':''}
    lista_combinaciones = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    turnos = 0
    while turnos <9:
        board.display_tablero(tab)
        correcto = board.juega_usuario(tab)
        if correcto:
            turnos +=1
            gana = check_winner(tab,lista_combinaciones)
            if gana == True:
                diccionario['ganador'] = "Jugador/a"
                print="¡Ganaste!"
                break
            ia(tab)
            gana = check_winner(tab,lista_combinaciones)
            if gana == True:
                diccionario['ganador'] = 'IA'
                print("¡Ganó la IA!")
                break
            turnos += 1
    board.display_tablero(tab)
    combinacion_ganadora(tab,lista_combinaciones)
    return diccionario
    
lista_combinaciones = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
def display_score(s:dict,d:dict):
    if d['ganador'] != '':
        print(f"El ganador fue {d['ganador']}")
        s[d['ganador']] +=1
    else:
        print("¡Empate!")
        s['Empates'] +=1
    print(f"<<Jugador:{s['Jugador/a']}>> <<IA:{s['IA']}>> <<Empates:{s['Empates']}>>")

def jugar_otra_vez():
    jugar = True
    otra_vez = input("¿Quieres jugar otra vez? (S/N)")
    otra_vez = otra_vez.upper()
    if (otra_vez != 'S'):
        juga = False
        print("¡Gracias por jugar!")
    return jugar
        
def two_player_game():
    tab_dict= {x:str(x) for x in tablero}
    diccionario = {'ganador':''}
    lista_combinaciones = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    turnos = 0
    while turnos <16:
        board.display_tablero(tab_dict)
        correcto = board.juega_usuario1(tab_dict)
        if correcto:
            turnos +=1
            gana = check_winner(tab_dict,lista_combinaciones)
            if gana == True:
                diccionario['ganador'] = "Jugador/a"
                print="¡Ganaste!"
                break
            board.display_tablero(tab_dict)
            correcto = board.juega_usuario2(tab_dict)
            if correcto:
                turnos +=1
                gana = check_winner(tab_dict,lista_combinaciones)
                if gana == True:
                    diccionario['ganador'] = "Jugador/a"
                    print="¡Ganaste!"
                    break
                turnos += 1
    board.display_tablero(tab_dict)
    combinacion_ganadora(tab_dict,lista_combinaciones)
    return diccionario

def game_cycle():
    score = {'Jugador/a':0, 'IA':0, 'Empates':0}
    continuar = True
    while continuar:
        #iniciamos el tablero
        tab_dict= {x:str(x) for x in tablero}
        # Cuantos jugadores van a ser?
        jugadores = input("¿Cuántos jugadores seran? (1/2)")
        if jugadores == '1':
            d = game(tab_dict)
            display_score(score,d)
            continuar = jugar_otra_vez()
        elif jugadores == '2':
            two_player_game()
            continuar = jugar_otra_vez()
        else:
            print("Opción no válida")
            game_cycle()
            

if __name__ == "__main__":
    game_cycle()
