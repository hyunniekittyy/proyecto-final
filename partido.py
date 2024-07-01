from equipo import Equipo
from estadio import Estadio


class Partido():
    def __init__(self, id: str, number: int, home: str, away: str, date: str, group: str, stadium_id: str) -> None:
        self.id =id
        self.number =number
        self.home =home
        self.away =away
        self.date =date
        self.group =group
        self.stadium_id =stadium_id

    def __str__(self):
        return f"id: {self.id}"
    
    def get_home(self, equipos: list[Equipo]):
        for equipo in equipos:
            if equipo.id ==  self.home:
                return equipo
        return None
    
    def get_away(self, equipos: list[Equipo]):
        for equipo in equipos:
            if equipo.id ==  self.away:
                return equipo
        return None
    
    def get_estadio(self,estadios: list[Estadio]):
        for estadio in estadios:
            if self.stadium_id == estadio.id:
                return estadio
        return None
    