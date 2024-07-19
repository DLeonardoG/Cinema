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
                Log_In_FaixApp_Artists()
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
                            if op_1_1_1 == "1":crear_cancion()
                            elif op_1_1_1 == "2":
                                while True:
                                    clear_screen()
                                    diseño_logo_artista()
                                    mostrar_txt(m_info)
                                    op_info = input("Seleccione una opcion:\n👉   ")
                                    line()
                                    if op_info == "1": crear_info()
                                    elif op_info == "2": break
                                    else: print ("opcion no valida")
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "2": 
                        while True:
                            clear_screen()
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_2)
                            op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_1_1_1 == "1": eliminar_cancion()
                            elif op_1_1_1 == "2":
                                while True:
                                    clear_screen()
                                    diseño_logo_artista()
                                    mostrar_txt(m_info)
                                    op_info = input("Seleccione una opcion:\n👉   ")
                                    line()
                                    if op_info == "1": eliminar_info()
                                    elif op_info == "2": break
                                    else: print ("opcion no valida")
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "3":
                        while True:
                            clear_screen()
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_3)
                            op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_1_1_1 == "1": actualizar_cancion()
                            elif op_1_1_1 == "2":
                                while True:
                                    clear_screen()
                                    diseño_logo_artista()
                                    mostrar_txt(m_info)
                                    op_info = input("Seleccione una opcion:\n👉   ")
                                    line()
                                    if op_info == "1": actualizar_info()
                                    elif op_info == "2": break
                                    else: print ("opcion no valida")
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "4": 
                        while True:
                            clear_screen()
                            diseño_logo_artista()
                            mostrar_txt(m_1_1_4)
                            op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_1_1_1 == "1": leer_cancion()
                            elif op_1_1_1 == "2":
                                while True:
                                    clear_screen()
                                    diseño_logo_artista()
                                    mostrar_txt(m_info_leer)
                                    op_info = input("Seleccione una opcion:\n👉   ")
                                    line()
                                    if op_info == "1": leer_info()
                                    elif op_info == "2": break
                                    else: print ("opcion no valida")
                            elif op_1_1_1 == "3": break
                            else: print ("opcion no valida")
                    elif op_1_1 == "5": break
                    else: print ("opcion no valida")
            elif op_login == "2": 
                clear_screen()
                diseño_logo_artista()
                Sign_Up_FaixApp_Artist()
            elif op_login == "3": break
            else: print ("opcion no valida")
    elif op == "2":
        while True:
            clear_screen()
            diseño_logo()
            mostrar_txt(m_login_d)
            op_login = input("Seleccione una opcion:\n👉   ")
            line()
            if op_login == "1":
                clear_screen()
                diseño_logo_discografia()
                Log_In_FaixApp_Artists()
                while True:
                    clear_screen()
                    diseño_logo()
                    mostrar_txt(m_1_2)
                    op_1_2 = input("Seleccione una opcion:\n👉   ")
                    line()
                    if op_1_2 == "1": leer_genero()
                    elif op_1_2 == "2": leer_artistas()
                    elif op_1_2 == "3": leer_canciones_artista()
                    elif op_1_2 == "4": leer_album()
                    elif op_1_2 == "5": crear_contrato()
                    elif op_1_2 == "6": break
                    else: print ("opcion no valida")
            elif op_login == "2": 
                clear_screen()
                diseño_logo_discografia()
                Sign_Up_FaixApp_Artist()
            elif op_login == "3": break
            else: print ("opcion no valida")
    elif op == "3":
        clear_screen()
        diseño_logo()
        print("A d i o s . . .")
        break
    else: print ("O p c i o n  n o  v a l i d a . . .")