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






