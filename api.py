import requests

from equipo import Equipo
from estadio import Estadio
from partido import Partido
from producto import Producto
from restaurante import Restaurante

def leer_equipos():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
    return data

def crear_equipos():
    data = leer_equipos()
    equipos = []
    equipos: list[Equipo] #opcional pero MUY util

    for equipo in data:
        nuevo_equipo = Equipo(equipo["id"],equipo["code"],equipo["name"], equipo["group"])
        equipos.append(nuevo_equipo)
    return equipos

def leer_partidos():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
    return data

def crear_partidos():
    data = leer_partidos()
    partidos = []
    partidos: list[Partido]
    for partido in data:
        nuevo_partido = Partido(partido["id"],partido["number"],partido["home"]["id"], partido["away"]["id"],partido["date"],partido["group"], partido["stadium_id"])
        partidos.append(nuevo_partido)
    return partidos

def leer_estadios():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
    return data

def crear_estadios():
    data = leer_estadios()

    estadios = []
    for estadio in data:
        restaurantes = []
        for restaurante in estadio["restaurants"]:
            productos = []
            productos: list[Producto]
            for producto in restaurante["products"]:
                nuevo_producto = Producto(producto["name"], producto["quantity"], producto["price"], producto["stock"], producto["adicional"])
                productos.append(nuevo_producto)
            nuevo_restaurante = Restaurante(restaurante["name"],productos)
            restaurantes.append(nuevo_restaurante)
        nuevo_estadio = Estadio(estadio["id"],estadio["name"],estadio["city"],estadio["capacity"],restaurantes)
        estadios.append(nuevo_estadio)
    return estadios


