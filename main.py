from importaciones import *


while True:
    clear_screen()
    diseño_logo()
    mostrar_txt(principal)
    op = input("Seleccione una opcion:\n👉   ")
    line()
    if op == "1":
        while True:
            clear_screen()
            diseño_logo()
            mostrar_txt(m_login_a)
            op_login = input("Seleccione una opcion:\n👉   ")
            line()
            if op_login == "1":
                clear_screen()
                diseño_logo_artista()
                login()
                while True:
                    clear_screen()
                    diseño_logo_artista()
                    mostrar_txt(m_1_1)
                    op_1_1 = input("Seleccione una opcion:\n👉   ")
                    line()
                    if op_1_1 == "1": 
                        while True:
                            clear_screen()
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_1)
                            op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_1_1_1 == "1": crear_funciones()
                            elif op_1_1_1 == "2": crear_pelicula()
                            elif op_1_1_1 == "3": break
                            else: 
                                print("Opción no válida")
                    elif op_1_1 == "2": 
                        while True:
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_2)
                            op_1_1_1 = input("Seleccione una opción:\n👉   ")
                            line()
                            if op_1_1_1 == "1": eliminar_funcion() 
                            elif op_1_1_1 == "2": eliminar_pelicula()
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "3":
                        while True:
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_3)
                            op_1_1_1 = input("Seleccione una opción:\n👉   ")
                            line()
                            if op_1_1_1 == "1": actualizar_funcion()
                            elif op_1_1_1 == "2": actualizar_pelicula()
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "4": 
                        while True:
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_4)
                            op_1_1_1 = input("Seleccione una opción:\n👉   ")
                            line()
                            if op_1_1_1 == "1": consultar_funciones()
                            elif op_1_1_1 == "2": consultar_pelicula()
                            elif op_1_1_1 == "3": consultar_funciones_porllave()
                            elif op_1_1_1 == "4": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "5": break
                    else: print ("opcion no valida")
            elif op_login == "2": 
                diseño_logo_artista()
                sign_up()
            elif op_login == "3": break
            else: print ("opcion no valida")
    elif op == "2":
        while True:
            clear_screen()
            diseño_logo()
            mostrar_txt(m_1_2)
            op_1_2 = input("Seleccione una opcion:\n👉   ")
            line()
            if op_1_2 == "1": crear_reserva()
            elif op_1_2 == "2": print ("cartelera")
            elif op_1_2 == "3": eliminar_reserva()
            elif op_1_2 == "4": break
            else: print ("opcion no valida")
    elif op == "3":
        diseño_logo()
        print("¡Adiós!")
        break
    else: print ("O p c i o n  n o  v a l i d a . . .")