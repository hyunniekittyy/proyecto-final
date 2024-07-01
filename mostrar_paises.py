from equipo import Equipo
from partido import Partido


def mostrar_todos_los_paises_con_indices(partidos: list[Partido], equipos: list[Equipo]):
    indice = 1
    for partido in partidos:
        print(str(indice) + f". {partido.get_home(equipos)}")
        indice += 1