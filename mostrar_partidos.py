from equipo import Equipo
from partido import Partido


def mostrar_partidos(partidos: list[Partido], equipos: list[Equipo]):
    for partido in partidos:
        print(partido.get_home(equipos), "vs", partido.get_away(equipos))

def mostrar_partidos_con_indice(partidos: list[Partido], equipos: list[Equipo]):
    indice = 1
    for partido in partidos:
        print(str(indice)+".-",partido.get_home(equipos), "vs", partido.get_away(equipos))
        indice += 1