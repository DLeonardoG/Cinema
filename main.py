from importaciones import *

while True:
    # clear_screen()
    diseño_logo()
    mostrar_txt(principal)
    op = input("Seleccione una opcion:\n👉   ")
    line()
    if op == "1":
        while True:
            # clear_screen()
            diseño_logo()
            mostrar_txt(m_login_a)
            op_login = input("Seleccione una opcion:\n👉   ")
            line()
            if op_login == "1":
                # clear_screen()
                diseño_logo_artista()
                login()
                while True:
                    # clear_screen()
                    diseño_logo_artista()
                    mostrar_txt(m_1_1)
                    op_1_1 = input("Seleccione una opcion:\n👉   ")
                    line()
                    if op_1_1 == "1": 
                        while True:
                            # clear_screen()
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_1)
                            op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_1_1_1 == "1":
                                # Crear función para crear una película
                                print ("pelicula_funciones.crear_funcion()")
                            elif op_1_1_1 == "2": 
                                # Crear función para crear una función
                                print ("pelicula_funciones.crear_peliculas()")
                            elif op_1_1_1 == "3": 
                                break
                            else: 
                                print("Opción no válida")
                    elif op_1_1 == "2": 
                        while True:
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_2)
                            op_1_1_1 = input("Seleccione una opción:\n👉   ")
                            line()
                            if op_1_1_1 == "1":
                                # Eliminar función
                                print ("pelicula_funciones.eliminar_funcion()")
                            elif op_1_1_1 == "2": 
                                # Eliminar película
                                print("pelicula_funciones.eliminar_pelicula()")
                            elif op_1_1_1 == "3": 
                                break
                            else: 
                                print("Opción no válida")
                    elif op_1_1 == "3":
                        while True:
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_3)
                            op_1_1_1 = input("Seleccione una opción:\n👉   ")
                            line()
                            if op_1_1_1 == "1":
                                # Actualizar función
                                print ("pelicula_funciones.actualizar_funcion()")
                            elif op_1_1_1 == "2": 
                                # Actualizar película
                                print ("pelicula_funciones.actualizar_pelicula()")
                            elif op_1_1_1 == "3": 
                                break
                            else: 
                                print("Opción no válida")
                    elif op_1_1 == "4": 
                        while True:
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_4)
                            op_1_1_1 = input("Seleccione una opción:\n👉   ")
                            line()
                            if op_1_1_1 == "1":
                                # Consultar función
                                print ("pelicula_funciones.consultar_funcion()")
                            elif op_1_1_1 == "2": 
                                # Consultar película
                                print("pelicula_funciones.consultar_pelicula()")
                            elif op_1_1_1 == "3": 
                                # Consultar salas
                                print ("pelicula_funciones.consultar_salas()")
                            elif op_1_1_1 == "4": 
                                break
                            else: 
                                print("Opción no válida")
                    elif op_1_1 == "5": 
                        break
                    else: 
                        print("Opción no válida")
            elif op_login == "2": 
                diseño_logo_artista()
                sign_up()
            elif op_login == "3": break
            else: print("Opción no válida")
    elif op == "2":
        while True:
            diseño_logo()
            mostrar_txt(m_1_2)
            op_1_2 = input("Seleccione una opción:\n👉   ")
            line()
            if op_1_2 == "1": crear_reserva()
            elif op_1_2 == "2": print("Cartelera")
            elif op_1_2 == "3": print("Próximamente")
            elif op_1_2 == "4": eliminar_reserva()
            elif op_1_2 == "5": break
            else: print("Opción no válida")
    elif op == "3":
        diseño_logo()
        print("¡Adiós!")
        break
    else: print("Opción no válida")

























