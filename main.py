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
                            if op_1_1_1 == "1":print ("crear_funcion()")
                            elif op_1_1_1 == "2": print ("crear_pelicula()")
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "2": 
                        while True:
                            # clear_screen()
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_2)
                            op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_1_1_1 == "1":print ("eliminar_funcion()")
                            elif op_1_1_1 == "2": print ("eliminar_pelicula()")
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "3":
                        while True:
                            # clear_screen()
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_3)
                            op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_1_1_1 == "1":print ("actualizar_funcion()")
                            elif op_1_1_1 == "2": print ("actualizar_pelicula()")
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "4": 
                        while True:
                            # clear_screen()
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_4)
                            op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_1_1_1 == "1":print ("consultar_funcion()")
                            elif op_1_1_1 == "2": print ("consultar_pelicula()")
                            elif op_1_1_1 == "3": print ("consultar_salas()")
                            elif op_1_1_1 == "4": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "5": break
                    else: print ("opcion no valida")
            elif op_login == "2": 
                # clear_screen()
                diseño_logo_artista()
                print ("sign up")
            elif op_login == "3": break
            else: print ("opcion no valida")
    elif op == "2":
        while True:
            # clear_screen()
            diseño_logo()
            mostrar_txt(m_login_d)
            op_login = input("Seleccione una opcion:\n👉   ")
            line()
            if op_login == "1":
                # clear_screen()
                diseño_logo_discografia()
                print ("login")
                while True:
                    # clear_screen()
                    diseño_logo()
                    mostrar_txt(m_1_2)
                    op_1_2 = input("Seleccione una opcion:\n👉   ")
                    line()
                    if op_1_2 == "1": print ("Reservar")
                    elif op_1_2 == "2": print ("cartelera")
                    elif op_1_2 == "3": print ("proximamente")
                    elif op_1_2 == "4": print ("cancelar")
                    elif op_1_2 == "5": break
                    else: print ("opcion no valida")
            elif op_login == "2": 
                # clear_screen()
                diseño_logo_discografia()
                print ("signup")
            elif op_login == "3": break
            else: print ("opcion no valida")
    elif op == "3":
        # clear_screen()
        diseño_logo()
        print("A d i o s . . .")
        break
    else: print ("O p c i o n  n o  v a l i d a . . .")