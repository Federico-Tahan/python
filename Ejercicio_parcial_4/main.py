__author__ = 'Algoritmos y Estructuras de Datos'

from funciones import *


def principal():
    v = []
    opcion = None

    while opcion != 8:
        print("📕📘" * 20)
        print("\t\t\t\t\t\t\t\t\t\tGestion de Autos")
        print("📕📘" * 20)
        print()
        print("1- Cargar arreglo")
        print("2- Sumar revision")
        print("3- Menor Votado")
        print("4- Popularidad 2000")
        print("5- Publicaciones por década")
        print()

        opcion = int(input("➡ Ingrese su opción: "))

        if opcion == 1:
            cargar_vector(v)
        elif len(v) > 0:
            if opcion == 2:
                mostrar_vector(v)
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                pass
        else:
            print('Primero debe cargar el arreglo de ventas de planes')


if __name__ == "__main__":
    principal()
