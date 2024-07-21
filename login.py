import json
import os
from funciones_secundarias import *

def cargar_datos_login(archivo):
    datos_login = {}
    with open(archivo,"r") as file:
        datos_login=json.load(file)
    return datos_login

def guardar_datos_login(archivo, datos_login):
    datos_login = dict(datos_login)
    
    diccionario=json.dumps(datos_login, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    
RUTA_BASE_DE_DATOS_LOGIN = "json\login.json"
datos_login = cargar_datos_login(RUTA_BASE_DE_DATOS_LOGIN)

def login_(datos_login: dict):
    print("Bienvenido admin")
    Correo = input("Ingrese su Correo: ")
    Contrasena_R = input("Ingrese su Contrasena: ")
    for i in range(len(datos_login["login"])):
        if datos_login["login"][i]["Correo"] == Correo:
            while datos_login["login"][i]["Contrasena"] != Contrasena_R:
                print("Contrasena Incorrecta")
                Contrasena_R = input("Ingrese su Contrasena: ")
            else:
                print ("")
                print("Inicio de sesión exitoso")
                print ("")
                return datos_login
    print ("")
    print("La cuenta no esta registrada")
    print ("")
    return datos_login
            
def login():
    datos_login = cargar_datos_login(RUTA_BASE_DE_DATOS_LOGIN)
    datos_login = login_(datos_login)
    guardar_datos_login(RUTA_BASE_DE_DATOS_LOGIN, datos_login)
    
    
def sign_up_(datos_login: dict):
    login = {}
    print("Bienvenido Usuario")
    login["Correo"] = input("Ingrese el Correo: ")
    while True:
        login["Contrasena"] = input("Cree una contrasena: ")
        contrasena_Ver = input("Verificar Contrasena: ")
        if login["Contrasena"] == contrasena_Ver:
            datos_login["login"].append(login)
            print("")
            print("Usuario Creado Exitosamente")
            print("")
            return datos_login
        else:
            print("Las Contrasenas no coinciden")
            return datos_login
            
def sign_up():
    datos_login = cargar_datos_login(RUTA_BASE_DE_DATOS_LOGIN)
    datos_login = sign_up_(datos_login)
    guardar_datos_login(RUTA_BASE_DE_DATOS_LOGIN, datos_login)
