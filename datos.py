import json

def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario = json.dumps(datos, indent=4)
    with open(archivo, "w", encoding="utf-8") as file:
        file.write(diccionario)
    
RUTA_BASE_DE_DATOS ="json/cine.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)