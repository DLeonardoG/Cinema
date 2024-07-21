import os
import platform
from datetime import datetime
import shutil

def time_now():
    fecha = datetime.now()
    fecha = fecha.replace(microsecond=0)
    return fecha
fecha = time_now()

def datetime_to_json(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

fecha = datetime_to_json(fecha)

def clear_screen():
    if platform.system() == 'Windows': os.system('cls')
    else: os.system('clear')

ARCHIVO = "errores.txt"
def reportar_error_a_txt(excepcion):
    ruta_errores = os.path.join("kaiosamapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: {excepcion}" 
        f.write(mensaje_error + '\n')
#opcion_no_valida()

def very():
    while True:
        linen()
        print_("¿Repetir operacion?")
        print_("1 .Si")
        print_("2 .No")
        continuar = input("                     >>>")
        linen()
        if continuar == "1": return "1"
        elif continuar == "2": 
            clear_screen()
            return "2"
        else: clear_screen()


def print_(*args, **kwargs):
    ancho_consola = shutil.get_terminal_size().columns
    texto = ' '.join(map(str, args))
    ancho_espacios = kwargs.get('ancho_espacios', 1)
    espacio_blancos = (ancho_consola - len(texto)) // 2
    print(' ' * espacio_blancos + texto.center(ancho_consola - 2 * espacio_blancos))


def line():
    ancho_consola = shutil.get_terminal_size().columns
    return print("-" * ancho_consola)

def linen():
    ancho_consola = shutil.get_terminal_size().columns
    return print("." * ancho_consola)
def linea():
    ancho_consola = shutil.get_terminal_size().columns
    return print("_" * ancho_consola)

def es():
    print(" ")

# def sala_de_cine():
#     ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
#     │ A1│ A2│ A3│ A4│ A5│ A6│ A7│ A8│ A9│A10│
#     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
#     │ B1│ B2│ B3│ B4│ B5│ B6│ B7│ B8│ B9│B10│
#     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
#     │ C1│ C2│ C3│ C4│ C5│ C6│ C7│ C8│ C9│C10│
#     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
#     │ D1│ D2│ D3│ D4│ D5│ D6│ D7│ D8│ D9│D10│
#     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
#     │ E1│ E2│ E3│ E4│ E5│ E6│ E7│ E8│ E9│E10│
#     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
def sillas_de_cine():
    # Secuencias de escape para el color azul
    BLUE = '\033[94m'
    RESET = '\033[0m'
    
    # Diseño de la maqueta sin sillas
    seating = f"""
    
        ==========================================
                     P A N T A L L A
    
        {BLUE}┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
        │ A1│ A2│ A3│ A4│ A5│ A6│ A7│ A8│ A9│A10│
        ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
        │ B1│ B2│ B3│ B4│ B5│ B6│ B7│ B8│ B9│B10│
        ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
        │ C1│ C2│ C3│ C4│ C5│ C6│ C7│ C8│ C9│C10│
        ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
        │ D1│ D2│ D3│ D4│ D5│ D6│ D7│ D8│ D9│D10│
        ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
        │ E1│ E2│ E3│ E4│ E5│ E6│ E7│ E8│ E9│E10│
        └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘{RESET}
    """
    print_(seating)


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

def seleccion_asiento():
    while True:
        cine_asientos()
        asiento = input("Seleccione un asiento (por ejemplo, A1): ").strip().upper()
        rows = ['A', 'B', 'C', 'D', 'E']
        columns = [str(i) for i in range(1, 11)]
        if len(asiento) == 2 and asiento[0] in rows and asiento[1:] in columns:
            cine_asientos(asiento)
            return asiento
        else:
            print("Asiento inválido. Inténtalo de nuevo.")





