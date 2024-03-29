from Athlete import Athlete
from Sport import Sport

class Team:
    def __init__(self,name:str,sport:Sport) -> None:
        self.name = name
        self.sport = sport
        self.players = []
    
    def add_player(self,athlete:Athlete):
        self.players.append(athlete)

    def display(self):
        print(f"Team {self.name}")
        print(f"{self.sport}")
        for athlete in self.players:
            print(f" {athlete}")

    def to_json(self)->dict:
        return {"name":self.name, "sport":self.sport.to_json(),
                "players": [p.name for p in self.players]
                }
    def __repr__(self) -> str:
        return f"Team('{self.name}',{self.players},{self.sport})"

if __name__ == "__main__":
    a = Athlete("Chicharito")
    b = Athlete("Piojo Alvarado")
    s = Sport("Soccer","11","LMX")
    t = Team("Chivas de Guadalajara",s)
    t.add_player(a)
    t.add_player(b)
    t.display()
    print(t.to_json())
        