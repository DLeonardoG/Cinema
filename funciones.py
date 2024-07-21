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

