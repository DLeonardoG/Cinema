import json


def cargar_datos(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        datos = json.load(file)
    return datos

def guardar_datos(datos, archivo):
    datos = dict(datos)
    diccionario = json.dumps(datos, indent=4)
    with open(archivo, "w", encoding="utf-8", ensure_ascii=False) as file:
        file.write(diccionario)
    
RUTA_BASE_DE_DATOS ="json/cine.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)