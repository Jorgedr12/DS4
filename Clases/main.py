from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json

def old_main():
    players = ['Chicharito','Piojo','Alexis Vega',
               'La Tota','Chuki','Tecatito',
               'Cuahutemoc','Hermoso','Piqué',
               'Messi','Ochoa'
               ]
    players_objects = [Athlete(x) for x in players]
    s = Sport("Soccer",11,"FIFA")
    t = Team("Dream Team",s)
    for a in players_objects:
        t.add_player(a)
    t.display()
    players_b = ['Iniesta','Xavi','Neymar','Hulk','Lewandoski','Puyol',
                 'Miguel','Aarón','Francisco','Maradona','Kaká']
    players_objects2 = [Athlete(x) for x in players_b]
    s2 = Sport("Soccer",11,"FIFA")
    t2 = Team("Equipo Ensueño",s2)
    for a in players_objects2:
        t2.add_player(a)
    torneo = { t.name:t.to_json(), t2.name:t2.to_json()}
    print(torneo)
    #torneo_json = json.dumps(torneo)
    
    with open("torneo_soccer.json","w", encoding="utf8") as archivo:
        archivo.write(str(torneo))
        
def old_main():
    players = ['Chicharito','Piojo','Alexis Vega',
               'La Tota','Chuki','Tecatito',
               'Cuahutemoc','Hermoso','Piqué',
               'Messi','Ochoa'
               ]
    players_objects = [Athlete(x) for x in players]
    s = Sport("Soccer",11,"FIFA")
    t = Team("Dream Team",s)
    for a in players_objects:
        t.add_player(a)
    t.display()
    players_b = ['Iniesta','Xavi','Neymar','Hulk','Lewandoski','Puyol',
                 'Miguel','Aarón','Francisco','Maradona','Kaká']
    players_objects2 = [Athlete(x) for x in players_b]
    s2 = Sport("Soccer",11,"FIFA")
    t2 = Team("Equipo Ensueño",s2)
    for a in players_objects2:
        t2.add_player(a)
    torneo = { t.name:t.to_json(), t2.name:t2.to_json()}
    print(torneo)
    #torneo_json = json.dumps(torneo)
    
    with open("torneo_soccer2.json","w", encoding="utf8") as archivo:
        archivo.write(str(torneo))

def procesa_diccionario(diccionario:dict)->dict:
    diccionario_equipos = {}
    for k1, v1 in diccionario.items():
        print(f"key1:{k1}")
        for k2, v2 in v1.items():
            print(f"  key2:{k2}")
            if (k2 == "players"):
                lista_atletas = [Athlete(x) for x in v2]
            if (k2 == 'sport'):
                sp_name  = v2['name']
                n_players= v2['num_players']
                league   = v2['league']
                s = Sport(sp_name,n_players,league)
                print(repr(s))
            if (k2 == 'name'):
                nombre_eq =v2
        equipo = Team(nombre_eq,s)
        for a in lista_atletas:
            equipo.add_player(a)
        print(repr(equipo))
        diccionario_equipos[k1] = equipo
    return diccionario_equipos


def main():
    opcion = input("Que torneo desea ver? (1/2) , \n 1.- Soccer \n 2.- Basketball \n =>")
    if (opcion == "1"):
        print("Soccer")
        with open("torneo_soccer.json","r",encoding="utf8") as archivo:
            json_leido = json.load(archivo)
        equipos = procesa_diccionario(json_leido)
        for equipo in equipos.items():
            print(equipo)
        lista_juegos = []
        lista_equipos = [k for k in equipos.keys()]
        while (len(lista_equipos)>=2):
            eq_casa = lista_equipos.pop(0)
            eqc = equipos[eq_casa]
            for eq_visitante in lista_equipos:
                eqv = equipos[eq_visitante]
                g = Game(eqc,eqv)
                g.play()
                lista_juegos.append(g)
                
        diccionario_score = {k:{"G":0,"P":0,"E":0} for k in equipos.keys()}
        print()
        print("Resultados:")
        for juego in lista_juegos:
            C = juego.A.name
            V = juego.B.name
            sc = juego.score[C]
            sv = juego.score[V]
            print(f"{C} {sc} - {sv} {V}")
            if (sc>sv):
                diccionario_score[C]["G"] +=1
                diccionario_score[V]["P"] +=1
            else:
                if (sc<sv):
                    diccionario_score[V]["G"] +=1
                    diccionario_score[C]["P"] +=1
                else:
                    diccionario_score[C]["E"] +=1
                    diccionario_score[V]["E"] +=1
        print()
        print("Score:")
        print(diccionario_score)
    else:
        if(opcion == "2"):
            print("Basketball")
            with open("torneo_basketball.json","r",encoding="utf8") as archivo:
                json_leido = json.load(archivo)
            equipos = procesa_diccionario(json_leido)
            for equipo in equipos.items():
                print(equipo)
            lista_juegos = []
            lista_equipos = [k for k in equipos.keys()]
            while (len(lista_equipos)>=2):
                eq_casa = lista_equipos.pop(0)
                eqc = equipos[eq_casa]
                for eq_visitante in lista_equipos:
                    eqv = equipos[eq_visitante]
                    g = Game(eqc,eqv)
                    g.play()
                    lista_juegos.append(g)
                
            diccionario_score = {k:{"G":0,"P":0,"E":0} for k in equipos.keys()}
            print()
            print("Resultados:")
            for juego in lista_juegos:
                C = juego.A.name
                V = juego.B.name
                sc = juego.score[C]
                sv = juego.score[V]
                print(f"{C} {sc} - {sv} {V}")
                if (sc>sv):
                    diccionario_score[C]["G"] +=1
                    diccionario_score[V]["P"] +=1
                else:
                    if (sc<sv):
                        diccionario_score[V]["G"] +=1
                        diccionario_score[C]["P"] +=1
                    else:
                        diccionario_score[C]["E"] +=1
                        diccionario_score[V]["E"] +=1
            print()
            print("Score:")
            print(diccionario_score)
                        
        else:
            print("Opcion no valida")
    
if __name__ == "__main__":
    main()



