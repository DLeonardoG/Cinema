import json
from diseños import *
from datos import *
from funciones_secundarias import *





def pelicula_existe(titulo):
    for pelicula in datos:
        if pelicula["nombre"].lower() == titulo.lower():
            return True
    return False




def crear_peliculas(datos:dict):
    while True:
        pelicula = {}
        diseño_logo_artista()
        print("Bienvenido al registro de películas")
        opcc = input("¿Desea registrar una película? (si o no): ")
        
        if opcc.lower() == "si":
            pelicula["nombre"] = input("Ingrese el nombre de la película: ")
            pelicula["clasificacion"] = input("Ingrese la clasificacion: ")
            pelicula["genero"] = input("Ingrese el genero de la película: ")
            pelicula["duracion"] = input("Ingrese el duracion de la pelicula: ")
            print("----------------------------------------------------------------------------------")
            pelicula["sinopsis"] = input("Ingrese una breve sinopsis de la película: ")
            print("----------------------------------------------------------------------------------")
            datos["peliculas"].append(pelicula)
            return datos
            # Agregar la película a la lista en memoria # Guardar los datos actualizados en el archivo JSON
        elif opcc.lower() == "no":
            return datos
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
            continue

def crear_pelicula():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = crear_peliculas(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

# crear_pelicula()
# Guardar los datos actualizados en el archivo JSON

def eliminar_peliculas(datos: dict):
    clear_screen()
    nombre =input("Ingrese el nombre de la pelicula: ").lower()
    for i in range(len(datos["peliculas"])):
        if datos["peliculas"][i]["nombre"] == nombre:
            datos["peliculas"].pop(i)
            print(f"La pelicula de",nombre," se ha eliminado con exito...")
            return datos
    print (f"La pelicula de ",nombre," no esta registrada...")    
    return datos

def eliminar_pelicula():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = eliminar_peliculas(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
#eliminar_pelicula()

def actualizar_peliculas(datos:dict):
    diseño_logo_artista()
    print("Actualización de Película")
    titulo = input("Ingrese el nombre de la película que desea actualizar: ")
    for i in range(len(datos["peliculas"])):
        if datos["peliculas"][i]["nombre"] == titulo:
            print("Datos actuales de la película:")
            print(f"nombre: {datos["peliculas"][i]["nombre"]}")
            print(f"clasificacion: {datos["peliculas"][i]['clasificacion']}")
            print(f"genero: {datos["peliculas"][i]['genero']}")
            print(f"duracion: {datos["peliculas"][i]['duracion']}")
            print("------------------------")
            
            # Solicitar al usuario los nuevos datos
            nuevo_titulo = input(f"Ingrese el nuevo nombre: ")
            nuevo_clasificacion = input(f"Ingrese la nueva clasificacion: ")
            nuevo_genero = input(f"Ingrese el nuevo genero: ")
            nuevo_duracion = input(f"Ingrese la nueva duracion: ")
            
            # Actualizar los datos en la lista en memoria
            datos["peliculas"][i]["nombre"] = nuevo_titulo
            datos["peliculas"][i]['clasificacion'] = nuevo_clasificacion
            datos["peliculas"][i]['genero'] = nuevo_genero
            datos["peliculas"][i]['duracion'] = nuevo_duracion
            print(f"Película {titulo} actualizada en la lista en memoria.")
            return datos
    
    print(f"No se encontró la película {titulo} en la lista en memoria.")
    return datos
    # Guardar los datos actualizados en el archivo JSON
def actualizar_pelicula():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = actualizar_peliculas(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

# actualizar_pelicula()

def consultar_peliculas(datos:dict):
    diseño_logo_artista()
    print("Consulta de Película")
    titulo = input("Ingrese el nombre de la película que desea consultar: ")
    # Cargar los datos desde el archivo JSON para reflejar cambios recientes
    for i in range(len(datos["peliculas"])):
        if datos["peliculas"][i]["nombre"] == titulo:
            print(f"Detalles de la película '{datos["peliculas"][i]["nombre"]}':")
            print(f"clasificacion: {datos["peliculas"][i]['clasificacion']}")
            print(f"genero: {datos["peliculas"][i]['genero']}")
            print(f"duracion: {datos["peliculas"][i]['duracion']}")
            print(f"sinopsis: {datos["peliculas"][i]['sinopsis']}")
            return datos
    print(f"No se encontró la película '{titulo}'.")
    return datos

def consultar_pelicula():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = consultar_peliculas(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# consultar_pelicula()

def consultar_salas():
    global datos
    diseños.diseño_logo_artista()
    print("Consulta de Salas")
    salas_disponibles = set()
    
    # Cargar los datos desde el archivo JSON para reflejar cambios recientes
    cargar_datos()
    
    for pelicula in datos:
        if 'Salas' in pelicula:
            for sala in pelicula['Salas']:
                salas_disponibles.add(sala)
    
    if salas_disponibles:
        print("Salas disponibles para proyección:")
        for sala in salas_disponibles:
            print(f"- {sala}")
    else:
        print("No se encontraron salas disponibles para proyección.")