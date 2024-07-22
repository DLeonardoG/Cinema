import json 

# Función para cargar datos desde el JSON 
def cargar_datos(nombre_archivo): 
    try: 
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            print ("Datos cargados exitosamente")
            return json.load(file)
    except Exception as e: 
        print(f"Error al cargar los datos {e}")

# Función para guardar datos en el JSON 
def guardar_datos(nombre_archivo, data): 
    try: 
        with open (nombre_archivo, "w", encoding="utf-8") as file: 
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e: 
        print(f"Error al guardar los datos: {e}")

# Función para mostrar los nombres de la películas 
def mostrar_peliculas():
    data = cargar_datos("json/cine.json")
    print("Películas disponibles:")
    for pelicula in data["peliculas"]:
        print(f"- {pelicula['nombre']}")

# Función que genera los id para las funciones
def id_funciones():
    data = cargar_datos("json/cine.json")
    if not data["funciones"]:
        return "0001"
    else:
        max_id = max(int(funcion["funciones_id"]) for funcion in data["funciones"])
        new_id = max_id + 1
        return f"{new_id:04d}"

# Función para crear funciones nuevas 
def crear_funciones(): 
    data = cargar_datos("json/cine.json")

    # Ingresa el nombre de la pelicula 
    peliculas_nombres = [pelicula["nombre"] for pelicula in data["peliculas"]]
    print("Películas disponibles: ")
    mostrar_peliculas()
    while True:
        pelicula = input("Ingrese el nombre de la película (o escriba 'salir' para cancelar): ").lower()
        if pelicula.lower() == 'salir':
            print("Proceso cancelado.")
            return
        # Verifica que la película exista en la lista de películas
        if pelicula not in peliculas_nombres:
            print("La película especificada no existe. Por favor, intente de nuevo.")
        else:
            break
    
    while True:
        # Ingresa la sala
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
        # Ingresa el horario
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
            
        # Verifica si la sala esta ocupada en ese horario
        repetido = False
        for funcion in data["funciones"]:
            if funcion["sala"] == sala and funcion["horario"] == horario:
                repetido = True
                print("Ya existe una función en la misma sala y horario. Por favor, ingrese una sala o horario diferente.")
                break
        
        if not repetido:
            break
    
     # Ingresa el tipo de función
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
    guardar_datos("json/cine.json", data)

def esperar_tecla():
    input("Presiona Enter para continuar...")
# Función para mostrar todas las funciones 
def consultar_funciones():
    data = cargar_datos("json/cine.json")
    
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
        esperar_tecla()

# Función para mostrar funciones según un parametro 
def consultar_funciones_porllave():
    data = cargar_datos("json/cine.json")

    # Verifica si no hay funciones disponibles
    if not data["funciones"]:
        print("No hay funciones disponibles.")
        return

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
        esperar_tecla()

# Función para eliminar funciones 
def eliminar_funcion():
    data = cargar_datos("json/cine.json")

    # Solicita el ID de la función a eliminar
    funcion_id = input("Ingrese el ID de la función que desea eliminar: ").strip()

    # Busca la función con el ID proporcionado
    funcion_encontrada = None
    for funcion in data["funciones"]:
        if funcion["funciones_id"] == funcion_id:
            funcion_encontrada = funcion
            break

    # Verifica si la función fue encontrada
    if not funcion_encontrada:
        print(f"No se encontró ninguna función con el ID: {funcion_id}")
        return

    # Mnuestra los detalles de la función encontrada y solicita la confirmación para eliminar
    print("Función encontrada:")
    print(f"ID: {funcion_encontrada['funciones_id']}")
    print(f"Película: {funcion_encontrada['pelicula']}")
    print(f"Sala: {funcion_encontrada['sala']}")
    print(f"Horario: {funcion_encontrada['horario']}")
    print(f"Tipo: {funcion_encontrada['tipo']}")
    confirmacion = input("¿Está seguro de que desea eliminar esta función? (si/no): ").strip().lower()

    # Verifica la confirmación antes de eliminar la función
    if confirmacion != 'si':
        print("Eliminación cancelada.")
        return

    # Elimina la función y guarda los cambios
    data["funciones"].remove(funcion_encontrada)
    guardar_datos("json/cine.json", data)
    print(f"La función con ID: {funcion_id} ha sido eliminada exitosamente.")

def actualizar_funcion():
    data = cargar_datos("json/cine.json")

    if not data["funciones"]:
        print("No hay funciones disponibles.")
        return

    # Solicita ID de la función a actualizar
    while True:
        id_funcion = input("Ingrese el ID de la función que desea actualizar (o escriba 'salir' para cancelar): ")
        if id_funcion.lower() == 'salir':
            print("Proceso cancelado.")
            return
        
        # Verifica si la función con el ID ingresado existe
        funcion_a_actualizar = next((funcion for funcion in data["funciones"] if funcion["funciones_id"] == id_funcion), None)
        if not funcion_a_actualizar:
            print("ID no encontrado. Intente de nuevo.")
        else:
            break

    # Muestra las opciones que se pueden actualizar 
    opciones_actualizacion = {
        "1": "pelicula",
        "2": "sala",
        "3": "horario",
        "4": "tipo"
    }

    while True:
        print("Opciones de actualización:")
        print("1. Actualizar película")
        print("2. Actualizar sala")
        print("3. Actualizar horario")
        print("4. Actualizar tipo de sala")
        opcion = input("Seleccione una opción (1-4) o escriba 'salir' para cancelar: ")
        if opcion.lower() == 'salir':
            print("Proceso cancelado.")
            return
        if opcion not in opciones_actualizacion:
            print("Opción no válida. Intente de nuevo.")
        else:
            clave = opciones_actualizacion[opcion]
            break
    
    # Actualiza la opción seleccionada 
    # Si la opción seleccionada fue pelicula 
    if clave == "pelicula":
        peliculas_nombres = [pelicula["nombre"].lower() for pelicula in data["peliculas"]]
        print("Películas disponibles: ")
        mostrar_peliculas()
        while True:
            nuevo_valor = input(f"Ingrese el nuevo valor para {clave} (o escriba 'salir' para cancelar): ").lower()
            if nuevo_valor == 'salir':
                print("Proceso cancelado.")
                return
            if nuevo_valor not in peliculas_nombres:
                print("La película especificada no existe. Intente de nuevo.")
            else:
                funcion_a_actualizar[clave] = nuevo_valor
                break
    # Si la opción seleccionada fue sala 
    elif clave == "sala":
        salas_permitidas = ["01", "02", "03", "04"]
        while True:
            nuevo_valor = input(f"Ingrese el nuevo valor para {clave} (01, 02, 03, 04) o escriba 'salir' para cancelar: ")
            if nuevo_valor.lower() == 'salir':
                print("Proceso cancelado.")
                return
            if nuevo_valor not in salas_permitidas:
                print("Sala no permitida. Las salas permitidas son: " + ", ".join(salas_permitidas))
            else:
                funcion_a_actualizar[clave] = nuevo_valor
                break
    # Si la opción seleccionada fue horario
    elif clave == "horario":
        horarios_permitidos = ["11:00", "14:00", "17:00", "20:00"]
        while True:
            nuevo_valor = input(f"Ingrese el nuevo valor para {clave} (11:00, 14:00, 17:00, 20:00) o escriba 'salir' para cancelar: ")
            if nuevo_valor.lower() == 'salir':
                print("Proceso cancelado.")
                return
            if nuevo_valor not in horarios_permitidos:
                print("Horario no permitido. Los horarios permitidos son: " + ", ".join(horarios_permitidos))
            else:
                funcion_a_actualizar[clave] = nuevo_valor
                break
    # Si la opción seleccionada fue tipo de sala 
    elif clave == "tipo":
        tipos_permitidos = ["2D", "3D"]
        while True:
            nuevo_valor = input(f"Ingrese el nuevo valor para {clave} (2D, 3D) o escriba 'salir' para cancelar: ").upper()
            if nuevo_valor.lower() == 'salir':
                print("Proceso cancelado.")
                return
            if nuevo_valor not in tipos_permitidos:
                print("Tipo no permitido. Los tipos permitidos son: " + ", ".join(tipos_permitidos))
            else:
                funcion_a_actualizar[clave] = nuevo_valor
                break
    
    # Guardar los cambios en el archivo JSON
    guardar_datos("json/cine.json", data)
    print("Función actualizada exitosamente.")


    #crear_funciones()
    #consultar_funciones() muestra todas las funciones 
    #consultar_funciones_porllave() muestra las funciones por parametro
    #eliminar_funcion() 
    #actualizar_funcion()

