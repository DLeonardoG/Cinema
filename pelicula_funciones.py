import json
import diseños

data = []
RUTA_ARCHIVO = "json\cine.json"

def guardar_datos():
    global data
    try:
        with open(RUTA_ARCHIVO, "w") as file:
            json.dump(data, file, indent=4)
        print("Datos guardados exitosamente en el archivo JSON!!")
    except Exception as e:
        print(f"Error al guardar datos en el archivo JSON: {e}")

def cargar_datos():
    global data
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            data = json.load(file)
        print("Datos cargados exitosamente desde el archivo JSON!!")
    except Exception as e:
        print(f"Error al cargar datos desde el archivo JSON: {e}")
        data = []





def pelicula_existe(titulo):
    for pelicula in data:
        if pelicula["Título"].lower() == titulo.lower():
            return True
    return False




def crear_peliculas():
    global data
    while True:
        pelicula = {}
        diseños.diseño_logo_artista()
        print("Bienvenido al registro de películas")
        opcc = input("¿Desea registrar una película? (si o no): ")
        
        if opcc.lower() == "si":
            pelicula["Título"] = input("Ingrese el título de la película: ")
            pelicula["Director"] = input("Ingrese el nombre del director: ")
            pelicula["Género"] = input("Ingrese el género de la película: ")
            pelicula["Año"] = input("Ingrese el año de lanzamiento: ")
            print("----------------------------------------------------------------------------------")
            pelicula["Sinopsis"] = input("Ingrese una breve sinopsis de la película: ")
            print("----------------------------------------------------------------------------------")
            data["peliculas"].append(pelicula)
            data["peliculas"].append(pelicula)# Agregar la película a la lista en memoria
            guardar_datos()  # Guardar los datos actualizados en el archivo JSON
        elif opcc.lower() == "no":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
            continue
        
crear_peliculas()

def eliminar_pelicula():
    global data
    diseños.diseño_logo_artista()
    print("Eliminación de Película")
    titulo = input("Ingrese el título de la película que desea eliminar: ")
    
    encontrada = False
    for i in range(len(data["peliculas"])):
        if data["peliculas"][i]["Título"] == titulo:
            data["peliculas"].pop(i)
            encontrada = True
            print(f"Película '{titulo}' eliminada de la lista en memoria.")
            break
    if not encontrada:
        print(f"No se encontró la película '{titulo}' en la lista en memoria.")
    guardar_datos()  # Guardar los datos actualizados en el archivo JSON

def actualizar_pelicula():
    global data
    diseños.diseño_logo_artista()
    print("Actualización de Película")
    titulo = input("Ingrese el título de la película que desea actualizar: ")
    
    encontrada = False
    for i in range(len(data["peliculas"])):
        if data["peliculas"][i]["Título"] == titulo:
            print("Datos actuales de la película:")
            print(f"Título: {pelicula['Título']}")
            print(f"Director: {pelicula['Director']}")
            print(f"Género: {pelicula['Género']}")
            print(f"Año: {pelicula['Año']}")
            print("------------------------")
            
            # Solicitar al usuario los nuevos datos
            nuevo_titulo = input(f"Ingrese el nuevo título (actual: {pelicula['Título']}): ") or pelicula['Título']
            nuevo_director = input(f"Ingrese el nuevo director (actual: {pelicula['Director']}): ") or pelicula['Director']
            nuevo_genero = input(f"Ingrese el nuevo género (actual: {pelicula['Género']}): ") or pelicula['Género']
            nuevo_año = input(f"Ingrese el nuevo año (actual: {pelicula['Año']}): ") or pelicula['Año']
            
            # Actualizar los datos en la lista en memoria
            data["peliculas"][i]["Título"] = nuevo_titulo
            data["peliculas"][i]['Director'] = nuevo_director
            data["peliculas"][i]['Género'] = nuevo_genero
            data["peliculas"][i]['Año'] = nuevo_año
            
            encontrada = True
            print(f"Película '{titulo}' actualizada en la lista en memoria.")
            break
    
    if not encontrada:
        print(f"No se encontró la película '{titulo}' en la lista en memoria.")
    
    guardar_datos()  # Guardar los datos actualizados en el archivo JSON

def consultar_pelicula():
    global data
    diseños.diseño_logo_artista()
    print("Consulta de Película")
    titulo_pelicula = input("Ingrese el título de la película que desea consultar: ")
    
    # Cargar los datos desde el archivo JSON para reflejar cambios recientes
    cargar_datos()
    
    encontrada = False
    for i in range(len(data["peliculas"])):
        if data["peliculas"][i]["Título"] == titulo_pelicula:
            print(f"Detalles de la película '{data["peliculas"][i]["Título"]}':")
            print(f"Director: {data["peliculas"][i]['Director']}")
            print(f"Género: {data["peliculas"][i]['Género']}")
            print(f"Año: {data["peliculas"][i]['Año']}")
            print(f"Sinopsis: {data["peliculas"][i]['Sinopsis']}")
            encontrada = True
            break
    
    if not encontrada:
        print(f"No se encontró la película '{titulo_pelicula}'.")

def consultar_salas():
    global data
    diseños.diseño_logo_artista()
    print("Consulta de Salas")
    salas_disponibles = set()
    
    # Cargar los datos desde el archivo JSON para reflejar cambios recientes
    cargar_datos()
    
    for pelicula in data:
        if 'Salas' in pelicula:
            for sala in pelicula['Salas']:
                salas_disponibles.add(sala)
    
    if salas_disponibles:
        print("Salas disponibles para proyección:")
        for sala in salas_disponibles:
            print(f"- {sala}")
    else:
        print("No se encontraron salas disponibles para proyección.")