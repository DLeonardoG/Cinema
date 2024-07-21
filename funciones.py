from datos import *
from funciones_secundarias import *
from diseños import *

def crear_reservas(datos: dict):
    reservas={}
    clear_screen()
    diseño_logo()
    print_ ("F U N C I O N E S  D I S P O N I B L E S")
    for sn in range(len(datos["funciones"])):
        print_(datos["funciones"][sn]["pelicula"].capitalize())
    reservas["cliente_id"]=input("Ingrese su numero de identificación: ")
    funcion = input("Ingrese la funcion que desea: ").lower()
    for i in range(len(datos["funciones"])):
        if datos["funciones"][i]["pelicula"] == funcion:
            reservas["funciones_id"]=datos["funciones"][i]["funciones_id"]
            reservas["pelicula"]=datos["funciones"][i]["pelicula"]
            reservas["sala"]=datos["funciones"][i]["sala"]
            reservas["horario"]=datos["funciones"][i]["horario"]
            print_(" la reserva de ",reservas["pelicula"]," registrado con éxito!")
            datos["reservas"].append(reservas)
            return datos
        
    print("La funcion no se encuentra disponible")
    return datos

def crear_reserva():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = crear_reservas(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

crear_reserva()

def eliminar_reserva_(datos: dict):
    clear_screen()
    nombre =input("Ingrese el numero de identificacion: ").lower()
    for i in range(len(datos["reservas"])):
        if datos["reservas"][i]["nombre"] == nombre:
            
            informacion = (datos["reservas"][i]["pelicula"])
            datos["reservas"].pop(i)
            separador = " "
            informacion = separador.join(map(str, informacion))
            print(informacion," se ha eliminado con exito...")
            return datos
    print (f"La reserva de ",nombre," no esta resgistrada...")    
    return datos

def eliminar_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = eliminar_reserva_(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()