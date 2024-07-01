from boleto import Boleto
from estadio import Estadio
from partido import Partido


def mostrar_asientos(estadios: list[Estadio], partido: Partido, es_vip: bool, boletos: list[Boleto]):
    estadio = partido.get_estadio(estadios)

    nro_asientos = estadio.capacity[0 if not es_vip else 1]
    asientos = []

    for numero_asiento in range(1, nro_asientos + 1):
        for boleto in boletos:
            if boleto.asiento == numero_asiento and boleto.partido.id == partido.id:
                numero_asiento = "ocupado"
        asientos.append(numero_asiento)
    
    columna = 1

    for asiento in asientos:
        if columna <= 10:
            print(asiento,end="- ")
            columna += 1
        else:
            print("\n"+str(asiento),end="- ")
            columna = 2
    return asientos

    
