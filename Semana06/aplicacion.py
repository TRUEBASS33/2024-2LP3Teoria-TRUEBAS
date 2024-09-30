# aplicacion.py

import gestion_archivos
import sys  # Importa el módulo sys para poder usar sys.exit()

def menu():
    print("""
    Menú:
    1. Crear archivo
    2. Eliminar archivo
    3. Agregar contenido
    4. Mostrar contenido de archivo
    5. Salir
    """)

def crear():
    nombre = input("Ingrese el nombre del archivo: ")
    contenido = input("Ingrese el contenido del archivo: ")
    gestion_archivos.crear_archivo(nombre, contenido)

def eliminar():
    nombre = input("Ingrese el nombre del archivo a eliminar: ")
    gestion_archivos.eliminar_archivo(nombre)

def agregar():
    nombre = input("Ingrese el nombre del archivo: ")
    contenido = input("Ingrese el contenido a agregar: ")
    gestion_archivos.agregar_contenido_archivo(nombre, contenido)

def listar():
    nombre = input("Ingrese el nombre del archivo: ")
    gestion_archivos.leer_archivo(nombre)

def salir():
    print("Saliendo del programa.")
    sys.exit()  # Utiliza sys.exit() para salir del programa

def error():
    print("Opción no válida, por favor seleccione una opción correcta.")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear()
        elif opcion == '2':
            eliminar()
        elif opcion == '3':
            agregar()
        elif opcion == '4':
            listar()
        elif opcion == '5':
            salir()
        else:
            error()

if __name__ == "__main__":
    main()
# aplicacion.py

import gestion_archivos
import sys  # Importa el módulo sys para poder usar sys.exit()

def menu():
    print("""
    Menú:
    1. Crear archivo
    2. Eliminar archivo
    3. Agregar contenido
    4. Mostrar contenido de archivo
    5. Salir
    """)

def crear():
    nombre = input("Ingrese el nombre del archivo: ")
    contenido = input("Ingrese el contenido del archivo: ")
    gestion_archivos.crear_archivo(nombre, contenido)

def eliminar():
    nombre = input("Ingrese el nombre del archivo a eliminar: ")
    gestion_archivos.eliminar_archivo(nombre)

def agregar():
    nombre = input("Ingrese el nombre del archivo: ")
    contenido = input("Ingrese el contenido a agregar: ")
    gestion_archivos.agregar_contenido_archivo(nombre, contenido)

def listar():
    nombre = input("Ingrese el nombre del archivo: ")
    gestion_archivos.leer_archivo(nombre)

def salir():
    print("Saliendo del programa.")
    sys.exit()  # Utiliza sys.exit() para salir del programa

def error():
    print("Opción no válida, por favor seleccione una opción correcta.")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear()
        elif opcion == '2':
            eliminar()
        elif opcion == '3':
            agregar()
        elif opcion == '4':
            listar()
        elif opcion == '5':
            salir()
        else:
            error()

if __name__ == "__main__":
    main()

