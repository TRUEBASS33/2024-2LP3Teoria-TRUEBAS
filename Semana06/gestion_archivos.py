# gestion_archivos.py

import os

def crear_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"Archivo '{nombre_archivo}' creado con éxito.")

def eliminar_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
        print(f"Archivo '{nombre_archivo}' eliminado con éxito.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")

def agregar_contenido_archivo(nombre_archivo, contenido):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(contenido)
        print(f"Contenido agregado al archivo '{nombre_archivo}'.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")

def leer_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        print(f"Contenido del archivo '{nombre_archivo}':\n{contenido}")
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")
