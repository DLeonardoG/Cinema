from importaciones import *
import pelicula_funciones


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
                print ("login")
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
                                pelicula_funciones.crear_funcion()
                            elif op_1_1_1 == "2": 
                                # Crear función para crear una función
                                pelicula_funciones.crear_peliculas()
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
                                pelicula_funciones.eliminar_funcion()
                            elif op_1_1_1 == "2": 
                                # Eliminar película
                                pelicula_funciones.eliminar_pelicula()
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
                                pelicula_funciones.actualizar_funcion()
                            elif op_1_1_1 == "2": 
                                # Actualizar película
                                pelicula_funciones.actualizar_pelicula()
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
                                pelicula_funciones.consultar_funcion()
                            elif op_1_1_1 == "2": 
                                # Consultar película
                                pelicula_funciones.consultar_pelicula()
                            elif op_1_1_1 == "3": 
                                # Consultar salas
                                pelicula_funciones.consultar_salas()
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
                print("Sign up")
            elif op_login == "3": 
                break
            else: 
                print("Opción no válida")
    elif op == "2":
        while True:
            diseño_logo()
            mostrar_txt(m_login_d)
            op_login = input("Seleccione una opción:\n👉   ")
            line()
            if op_login == "1":
                diseño_logo_discografia()
                print("Login")
                while True:
                    diseño_logo()
                    mostrar_txt(m_1_2)
                    op_1_2 = input("Seleccione una opción:\n👉   ")
                    line()
                    if op_1_2 == "1": 
                        print("Reservar")
                    elif op_1_2 == "2": 
                        print("Cartelera")
                    elif op_1_2 == "3": 
                        print("Próximamente")
                    elif op_1_2 == "4": 
                        print("Cancelar")
                    elif op_1_2 == "5": 
                        break
                    else: 
                        print("Opción no válida")
            elif op_login == "2": 
                diseño_logo_discografia()
                print("Signup")
            elif op_login == "3": 
                break
            else: 
                print("Opción no válida")
    elif op == "3":
        diseño_logo()
        print("¡Adiós!")
        break
    else: 
        print("Opción no válida")

























