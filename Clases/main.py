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


def procesa_diccionario(diccionario:dict)->dict:
    diccionario_equipo = {}
    for k1,v1 in diccionario.items():
        print(f"key1:{k1}")
        for k2,v2 in v1.items():
            print(f"key2:{k2}")
            if (k2=="players"):
                lista_atletas = [Athlete(x) for x in v2]
            if (k2=="sport"):
                sp_name = v2['name']
                n_players = v2['num_players']
                league = v2['league']
                s = Sport(sp_name,n_players,league)
                print(repr(s))
            if (k2=="name"):
                nombre_eq = v2
        equipo = Team(nombre_eq,s)
        for a in lista_atletas:
            equipo.add_player(a)
        print(repr(equipo))
        diccionario_equipo[k1] = equipo
    return diccionario_equipo
                
                
def main():
    with open("torneo_soccer.json","r", encoding="utf8") as archivo:
        json_leido = json.load(archivo)
    equipos = procesa_diccionario(json_leido)
    for equipo in equipos.items():
        print(equipo)

if __name__ == "__main__":
    main()
