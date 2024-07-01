import api
from boleto import Boleto
import buscar_partidos
from cliente import Cliente
import venta_entradas

def main():

    while True:
        try:
            equipos = api.crear_equipos()
            partidos = api.crear_partidos()
            estadios = api.crear_estadios()
            clientes = []
            clientes: list[Cliente]
            boletos = []
            boletos: list[Boleto]

            inicio = input('''¿Que quieres hacer?
1.- Buscar partidos
2.- Comprar entradas
> ''')
    
            if inicio == "1":
                buscar_partidos.buscar_partidos(partidos, equipos, estadios)
            elif inicio == "2":
                venta_entradas.inicio_sesion(clientes,partidos, equipos, estadios, boletos)
        except:
            pass

main()