from secundary_funciones import fecha,os,line

def mostrar_txt(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Se produjo un error al intentar leer el archivo: {e}")
        

principal = "txt/main_plantillas/principal.txt"

#Menu admin
m_1 = "txt/main_plantillas/principal.txt"
m_1_1 = "txt/main_plantillas/admin/1-1.txt"
m_1_1_1 = "txt/main_plantillas/admin/1-1-1.txt"
m_1_1_2 = "txt/main_plantillas/admin/1-1-2.txt"
m_1_1_3 = "txt/main_plantillas/admin/1-1-3.txt"
m_1_1_4 = "txt/main_plantillas/admin/1-1-4.txt"
m_info = "txt/main_plantillas/admin/info.txt"
m_info_leer = "txt/main_plantillas/admin/info_leer.txt"

#Menu user
m_1_2 = "txt/main_plantillas/user/1-2.txt"
m_1_2_1 = "txt/main_plantillas/user/1-2-1.txt"
m_1_2_2 = "txt/main_plantillas/user/1-2-2.txt"
m_1_2_3 = "txt/main_plantillas/user/1-2-3.txt"

#Login 
m_login_a = "txt/main_plantillas/login/login_admin.txt"
m_login_d = "txt/main_plantillas/login/login_discograficas.txt"