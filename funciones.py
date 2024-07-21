import datos as dataOpciones
import json

def mostrar_peliculas():
    data = dataOpciones.cargar_datos("json/cine.json")
    print("Películas disponibles:")
    for pelicula in data["peliculas"]:
        print(f"- {pelicula['nombre']}")

def id_funciones():
    data = dataOpciones.cargar_datos("json/cine.json")
    if not data["funciones"]:
        return "0001"
    else:
        max_id = max(int(funcion["funciones_id"]) for funcion in data["funciones"])
        new_id = max_id + 1
        return f"{new_id:04d}"
    
def crear_funciones(): 
    data = dataOpciones.cargar_datos("json/cine.json")

    # Ingresar el nombre de la pelicula 
    peliculas_nombres = [pelicula["nombre"] for pelicula in data["peliculas"]]
    print("Películas disponibles: ")
    mostrar_peliculas()
    while True:
        pelicula = input("Ingrese el nombre de la película (o escriba 'salir' para cancelar): ").lower()
        if pelicula.lower() == 'salir':
            print("Proceso cancelado.")
            return
        # Verificar que la película exista en la lista de películas
        if pelicula not in peliculas_nombres:
            print("La película especificada no existe. Por favor, intente de nuevo.")
        else:
            break
    
    while True:
        # Ingresar la sala
        while True:
            salas_permitidas = ["01", "02", "03", "04"]
            sala = input("Ingrese la sala (01, 02, 03, 04) o escriba 'salir' para cancelar: ")
            if sala.lower() == 'salir':
                print("Proceso cancelado.")
                return
            if sala not in salas_permitidas:
                print("Sala no permitida. Las salas permitidas son: " + ", ".join(salas_permitidas))
            else:
                break
        # Ingresar el horario
        while True:
            horarios_permitidos = ["11:00", "14:00", "17:00", "20:00"]
            horario = input("Ingrese el horario (11:00, 14:00, 17:00, 20:00) o escriba 'salir' para cancelar: ")
            if horario.lower() == 'salir':
                print("Proceso cancelado.")
                return
            if horario not in horarios_permitidos:
                print("Horario no permitido. Los horarios permitidos son: " + ", ".join(horarios_permitidos))
            else:
                break
            
        # Verificar si la sala esta ocupada en ese horario
        repetido = False
        for funcion in data["funciones"]:
            if funcion["sala"] == sala and funcion["horario"] == horario:
                repetido = True
                print("Ya existe una función en la misma sala y horario. Por favor, ingrese una sala o horario diferente.")
                break
        
        if not repetido:
            break
    
     # Ingresar el tipo de función
    while True:
        tipos_permitidos = ["2D", "3D"]
        tipo = input("Ingrese el tipo (2D, 3D) o escriba 'salir' para cancelar: ").upper()
        if tipo.lower() == 'salir':
            print("Proceso cancelado.")
            return
        if tipo not in tipos_permitidos:
            print("Tipo no permitido. Los tipos permitidos son: " + ", ".join(tipos_permitidos))
        else:
            break

    # Creación de la función para guardar en el JSON
    nueva_funcion = {
        "funciones_id": id_funciones(),
        "pelicula": pelicula,
        "sala": sala,
        "horario": horario,
        "tipo": tipo
    }

    data["funciones"].append(nueva_funcion)
    dataOpciones.guardar_datos("json/cine.json", data)

def consultar_funciones():
    data = dataOpciones.cargar_datos("json/cine.json")
    
    # Verifica si no hay funciones disponibles
    if not data["funciones"]:
        print("No hay funciones disponibles.")
        return
    
    # Muestra todas las funciones disponibles 
    print("Funciones disponibles:")
    print("-" * 50)
    for funcion in data["funciones"]:
        print(f"- ID: {funcion['funciones_id']}")
        print(f"- Película: {funcion['pelicula']}")
        print(f"- Sala: {funcion['sala']}")
        print(f"- Horario: {funcion['horario']}")
        print(f"- Tipo: {funcion['tipo']}")
        print("-" * 50)

def consultar_funciones_porllave():
    data = dataOpciones.cargar_datos("json/cine.json")

    # Define las opciones de búsqueda disponibles
    opciones_busqueda = {
        "1": "funciones_id",
        "2": "pelicula",
        "3": "sala",
        "4": "horario",
        "5": "tipo"
    }

    # Muestra al administrador las opciones de búsqueda
    print("Opciones de búsqueda:")
    print("1. ID")
    print("2. Película")
    print("3. Sala")
    print("4. Horario")
    print("5. Tipo")

    # Solicita las opciones de búsqueda hasta que se ingrese una opción válida o se escriba 'salir'
    while True:
        opcion = input("Seleccione una opción de búsqueda (1-5) o escriba 'salir' para cancelar: ").lower()
        if opcion == 'salir':
            print("Proceso cancelado.")
            return
        if opcion in opciones_busqueda:
            break
        print("Opción no válida. Intente de nuevo.")

    # Obtiene la llave correspondiente a la opción seleccionada
    llave = opciones_busqueda[opcion]

    # Solicita el valor para la llave seleccionada
    valor = input(f"Ingrese el valor para {llave} o escriba 'salir' para cancelar: ").lower()
    if valor == 'salir':
        print("Proceso cancelado.")
        return

    # Busca las funciones que coincidan con el valor ingresado para la llave seleccionada
    funciones_encontradas = [funcion for funcion in data["funciones"] if funcion[llave].lower() == valor]

    # Verifica si se encontraron funciones
    if not funciones_encontradas:
        print(f"No se encontraron funciones para {llave}: {valor}")
        return

    # Muestra las funciones encontradas
    print(f"Funciones encontradas para {llave}: {valor}")
    print("-" * 50)
    for funcion in funciones_encontradas:
        print(f"ID: {funcion['funciones_id']}")
        print(f"Película: {funcion['pelicula']}")
        print(f"Sala: {funcion['sala']}")
        print(f"Horario: {funcion['horario']}")
        print(f"Tipo: {funcion['tipo']}")
        print("-" * 50)


