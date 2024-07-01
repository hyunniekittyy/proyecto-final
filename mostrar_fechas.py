from partido import Partido


def mostrar_fechas_con_indices(partidos: list[Partido]):
    fechas = []
    indice = 1
    for partido in partidos:
        if partido.date not in fechas:
            fechas.append(partido.date)
            print(str(indice) + f") {partido.date}")
            indice += 1
    return fechas