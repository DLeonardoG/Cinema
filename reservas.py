from datos import *
from funciones_secundarias import *
from diseños import *

def mostrar_cartelera(datos: dict): 
    clear_screen()
    diseño_logo()
    print_ ("F U N C I O N E S  D I S P O N I B L E S")
    for sn in range(len(datos["funciones"])):
        print_("- ID: ", datos["funciones"][sn]["funciones_id"].capitalize())
        print_("- Película: ", datos["funciones"][sn]["pelicula"].capitalize())
        print_("- Horario: ", datos["funciones"][sn]["horario"].capitalize())
        print_( "-" * 30)
    return datos

def cartelera():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = mostrar_cartelera(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

def cine_asientos(asiento=None):
    # Secuencias de escape para el color azul y rojo
    BLUE = '\033[94m'
    RED = '\033[91m'
    
    # Definición de las filas y columnas
    rows = ['A', 'B', 'C', 'D', 'E']
    columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    
    # Crear una maqueta base con todos los asientos
    seating = ""
    seating += f"{BLUE}┌───┬" + "───┬" * (len(columns) - 2) + "────┐\n"
    print("""
==========================================
             P A N T A L L A
""")
    for row in rows:
        seating += "│ "
        for col in columns:
            seat = f"{row}{col}"
            if seat == asiento:
                seating += f"{RED}{seat}{BLUE}│ "
            else:
                seating += f"{BLUE}{seat}{BLUE}│ "
        seating += "\n"
        if row != rows[-1]:
            seating += f"{BLUE}├───┼" + "───┼" * (len(columns) - 2) + "────┤\n"
        else:
            seating += f"{BLUE}└───┴" + "───┴" * (len(columns) - 2) + "────┘\n"
    
    print(seating)



def crear_reservas(datos: dict):
    reservas={}
    clear_screen()
    diseño_logo()
    print_ ("F U N C I O N E S  D I S P O N I B L E S")
    for sn in range(len(datos["funciones"])):
        print_("- ID: ", datos["funciones"][sn]["funciones_id"].capitalize())
        print_("- Película: ", datos["funciones"][sn]["pelicula"].capitalize())
        print_("- Horario: ", datos["funciones"][sn]["horario"].capitalize())
        print_( "-" * 30)
    reservas["cliente_id"]=input("Ingrese su numero de identificación: ")
    funcion = input("Ingrese el ID de la función que desea reservar: ").lower()
    for i in range(len(datos["funciones"])):
        if datos["funciones"][i]["funciones_id"] == funcion:
            reservas["funciones_id"]=datos["funciones"][i]["funciones_id"]
            reservas["pelicula"]=datos["funciones"][i]["pelicula"]
            reservas["sala"]=datos["funciones"][i]["sala"]
            reservas["horario"]=datos["funciones"][i]["horario"]
            
            while True:
                asi = input ("Cuantos asientos va a reservar: ")
                try:
                    asi = int(asi)
                    break
                except ValueError:
                    print("Inténtalo de nuevo.")
            reservas["asientos"]=[]
            for i in range(asi):
                while True:
                    cine_asientos()
                    asiento = input("Seleccione un asiento (por ejemplo, A1): ").strip().upper()
                    rows = ['A', 'B', 'C', 'D', 'E']
                    columns = [str(i) for i in range(1, 11)]
                    if len(asiento) == 2 or len(asiento) == 3 and asiento[0] in rows and asiento[1:] in columns:
                        for i in range(len(datos["reservas"])):
                            if datos["reservas"][i]["finciones_id"] == funcion:
                                for reserva in datos["reservas"]:
                                    for silla in reserva["asientos"]:
                                        if silla.lower() == asiento.lower():
                                            print("Este asiento ya está reservado. Inténtalo de nuevo.")
                                            continue
                                        
                                        
                                # for i in range(len(datos["reservas"][i]["asientos"])):
                                #     if datos["reservas"][i]["asientos"] == funcion:
                                #         cine_asientos(asiento)
                            
        else:
            print("Asiento inválido. Inténtalo de nuevo.")
                reservas["asientos"].append(selec)
            precio = 6000 * asi
            reservas["precio"]=precio
            
            print_("La reserva de ",reservas["pelicula"]," ha sido registrada a ",reservas["cliente_id"]," con éxito!")
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

# crear_reserva()

def eliminar_reservas(datos: dict):
    clear_screen()
    nombre =input("Ingrese el numero de identificacion: ").lower()
    for i in range(len(datos["reservas"])):
        if datos["reservas"][i]["cliente_id"] == nombre:
            datos["reservas"].pop(i)
            print(f"La reserva de",nombre," se ha eliminado con exito...")
            return datos
    print (f"La reserva de ",nombre," no esta resgistrada...")    
    return datos

def eliminar_reserva():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = eliminar_reservas(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
#eliminar_reserva()