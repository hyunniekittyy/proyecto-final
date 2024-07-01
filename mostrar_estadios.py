from estadio import Estadio


def mostrar_todos_los_estadios_con_indices(estadios: list[Estadio]):
    indice = 1
    for estadio in estadios:
        print(str(indice) + f". {estadio}")
        indice += 1