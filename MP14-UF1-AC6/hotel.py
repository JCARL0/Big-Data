"""
Programa de reserva de un hotel
Versión: 0.1
Author: A.Guardiola
"""
import json #Del módulo json sólo se utilizará la función dumps(), que sirve para imprimir de
            # manera amigable los diccionarios ("pretty printing") 

# SECCIÓN 1: INICIALIZACIÓN DE VARIABLES GLOBALES ###########################################

# Declaramos la variable hotel
hotel = [[{},{},{},{},{}],      # piso 1: 5 habitaciones sin inicializar
         [{},{},{},{},{}],      # piso 2: 5 habitaciones sin inicializar
         [{},{},{},{},{}],      # piso 3: 5 habitaciones sin inicializar
         [{},{},{},{},{}]]      # piso 4: 5 habitaciones sin inicializar

# Inicializamos las distintas habitaciones del hotel
    # (Esta sección podría estar incluida en una función inicializarHotel)
for piso, habitaciones in enumerate(hotel):                 # iteramos pisos   
    for numHab, habitacion in enumerate(habitaciones):      # iteramos habitaciones
        habitacion["numero"] = (piso+1)*10 + (numHab+1)     # inicializamos cada habitación
        habitacion["ocupada"] = False
        habitacion["fechaIngreso"] = ""
        habitacion["numNoches"] = 0
        if numHab + 1 == 1:
            habitacion["clase"] = "suite"
        else:
            habitacion["clase"] = "normal"
        habitacion["precio"] =0.0

# SECCIÓN 2: DECLARACIÓN DE FUNCIONES ######################################################

# Función 'hacerReserva' para rellenar una habitación con una reserva
def hacerReserva(piso,hab,fechaIngreso,numNoches):
    habitacion = hotel[piso-1][hab-1]
    habitacion["ocupada"] = True
    habitacion["fechaIngreso"] = fechaIngreso
    habitacion["numNoches"] = numNoches
    if hab == 1:
        habitacion["precio"] = habitacion["numNoches"] * 100
    else:
        habitacion["precio"] = habitacion["numNoches"] * 50
    return None

# SECCIÓN 2: DECLARACIÓN DE FUNCIONES ######################################################

# Función 'consultarReserva' que muestra por pantalla los datos de la reserva si la habitación
# está ocupada o el mensaje "Habitación sin reserva" en caso contrario
def consultarReserva(numHab):
    habitacion = None
    for piso in hotel:
        for hab in piso:
            if hab["numero"] == numHab and hab["ocupada"]:
                habitacion = hab
                break

    if habitacion:
        print("Datos de la reserva:")
        print(f"Número de habitación: {habitacion['numero']}")
        print(f"Fecha de ingreso: {habitacion['fechaIngreso']}")
        print(f"Noches reservadas: {habitacion['numNoches']}")
        print(f"Tipo de habitación: {habitacion['clase']}")
        print(f"Precio de reserva: {habitacion['precio']}")
    else:
        print("Habitación sin reserva")

# Función 'anularReserva' para eliminar la reserva de una habitación
# La habitación debe devolverse a su estado inicial
def anularReserva(numHab):
    for piso in hotel:
        for hab in piso:
            if hab["numero"] == numHab:
                hab["ocupada"] = False
                hab["fechaIngreso"] = ""
                hab["numNoches"] = 0
                hab["precio"] = 0.0
                break

# Función 'modificarReserva' para modificar la reserva de una habitación
# La función sólo debe dejar modificar las claves "fechaIngreso" y "numNoches"
# La función debe recalcular el precio de la reserva
def modificarReserva(clave, valorNuevo):
    if clave in ["fechaIngreso", "numNoches"]:
        for piso in hotel:
            for hab in piso:
                if hab["ocupada"]:
                    hab[clave] = valorNuevo
                    if hab["clase"] == "suite":
                        hab["precio"] = hab["numNoches"] * 100
                    else:
                        hab["precio"] = hab["numNoches"] * 50

# Función 'listarOcupadas' que devuelve la lista de habitaciones ocupadas
def listarOcupadas():
    habsOcupadas = []
    for piso in hotel:
        for hab in piso:
            if hab["ocupada"]:
                habsOcupadas.append(hab["numero"])
    return habsOcupadas

# Función 'estaLibre' que devuelve False si la habitación está ocupada y True si está libre
def estaLibre(numHab):
    for piso in hotel:
        for hab in piso:
            if hab["numero"] == numHab:
                return not hab["ocupada"]

# SECCIÓN 3: PROGRAMA PRINCIPAL ###########################################################

print(json.dumps(hotel, indent=4))        # Mostramos estado inicial del hotel
hacerReserva(3, 1, "20221117", 4)         # Hacemos tres reservas
hacerReserva(1, 3, "20221123", 5)
hacerReserva(4, 2, "20221201", 1)
print(json.dumps(hotel, indent=4))        # Mostramos estado del hotel

# Probamos las funciones implementadas
consultarReserva(23)
anularReserva(23)
consultarReserva(23)
modificarReserva("fechaIngreso", "20221203")
modificarReserva("numNoches", 3)
consultarReserva(23)
print("Habitaciones ocupadas:", listarOcupadas())
print("¿Está libre la habitación 23?", estaLibre(23))
