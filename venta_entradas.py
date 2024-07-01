from boleto import Boleto
from cliente import Cliente
from equipo import Equipo
from estadio import Estadio
from partido import Partido
import mostrar_partidos
import mostrar_asientos


def inicio_sesion(clientes: list[Cliente], partidos: list[Partido], equipos: list[Equipo], estadios: list[Estadio], boletos: list[Boleto]):
    while True:
        nuevo_usuario = es_nuevo_usuario()

        if nuevo_usuario:
            nombre = preguntar("Ingrese nombre: ")
            ci = preguntar_numero("Ingrese ci: ")
            contrasena = preguntar("Ingrese contrasena: ")
            age = preguntar_numero("Ingrese edad: ")
            #TODO: validar que no exista ya un cliente con la cedula que ingresó el usuario 
            nuevo_cliente = Cliente(nombre, age, ci, contrasena)
            clientes.append(nuevo_cliente)
        else:
            nuevo_cliente = iniciar_sesion(clientes)

        if nuevo_cliente:
            partido_seleccionado = preguntar_partido_especifico(partidos, equipos)
            print("va a preguntar si es vip")
            es_vip = preguntar_tipo_entrada()

            # print("Elije uno: ")
            # asientos = mostrar_asientos.mostrar_asientos(estadios,partido_seleccionado,es_vip,boletos)
            # asiento = input("> ")
            
            asiento_seleccionado = preguntar_asientos(estadios,partido_seleccionado,es_vip,boletos)

            es_vampiro = nuevo_cliente.su_cedula_es_vampiro()
            print("Es vampiro" if es_vampiro else "No es vampiro")

            boleto = Boleto(asiento_seleccionado,nuevo_cliente.ci,partido_seleccionado)
            boletos.append(boleto)
            print(f"asiento {str(asiento_seleccionado)} comprado exitosamente")

def preguntar_asientos(estadios,partido_seleccionado,es_vip,boletos):
    while True:
        try:
            print("Elije uno: ")
            asientos = mostrar_asientos.mostrar_asientos(estadios,partido_seleccionado,es_vip,boletos)
            asiento = int(input("> "))

            if asiento in asientos:
                return asiento
            print("Asiento inválido")
        except:
            pass


def preguntar_tipo_entrada():
    while True:
        try:
            pregunta = input("Es vip? (y o n): ")
            if pregunta.lower() == "y": return True
            if pregunta.lower() == "n": return False
        except:
            pass



def preguntar_partido_especifico(partidos, equipos):
    while True:
        try:
            print("Elige el partido que desees comprar sus entradas:")
            mostrar_partidos.mostrar_partidos_con_indice(partidos, equipos)
            pregunta = int(input("> "))
            print("lo va a buscar")
            partido_seleccionado = partidos[pregunta - 1]
            print("lo encontro")
            return partido_seleccionado
        except Exception as e:
            print("error")
            pass


def iniciar_sesion(clientes: list[Cliente]):
    while True:
        try:
            cedula = int(input("ingrese cedula: "))
            password = input("ingrese contrasenia: ")

            for cliente in clientes:
                if cliente.ci == cedula and cliente.password == password:
                    return cliente
            print("Ese cliente no existe")
            continuar = input("¿Volver a intentar? (y or n):")
            if continuar == "n":
                return False
        except:
            pass


def preguntar(mensaje: str):
    while True:
        try:
            pregunta = input(mensaje)

            if pregunta == "":
                continue

            return pregunta
        except:
            pass

def preguntar_numero(mensaje: str):
    while True:
        try:
            pregunta = int(input(mensaje))
            return pregunta
        except:
            pass



def es_nuevo_usuario():
    while True:
        pregunta = input('''¿Que quieres hacer=
1.- Iniciar sesión
2.- Registrarme
> ''')
        if pregunta == '1':
            return False
        elif pregunta == "2":
            return True