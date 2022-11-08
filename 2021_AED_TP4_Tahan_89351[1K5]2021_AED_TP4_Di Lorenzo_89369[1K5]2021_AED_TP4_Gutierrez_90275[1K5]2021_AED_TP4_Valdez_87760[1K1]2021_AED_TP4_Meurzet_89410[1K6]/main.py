
from trabajar_archivo import *
from funciones import *

NAME = "populares.dat"


def principal():
    v = []
    matriz = None
    opcion = None
    while opcion != 8:
        print("📕📘" * 60)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t📕📘 Gestion de Libros v2.0 📘📕")
        print("📕📘" * 60)
        print()
        print("1- Cargar arreglo")
        print("2- Sumar revision")
        print("3- Menor Votado")
        print("4- Popularidad 2000")
        print("5- Publicaciones por década")
        print("6- Guardar populares")
        print("7- Mostrar Archivos")
        print("8- Finalizar Programa")
        print()

        opcion = int(input("➡ Ingrese su opción: "))

        if opcion == 1:
            generar_arreglo(v)
            print("\n ✔ El arreglo ha sido cargado con exito!")
        elif opcion == 2:
            if not v:
                print("❌ No hay datos cargados para la busqueda")
            else:
                search_book(v)
        elif opcion == 3:
            if not v:
                print("❌ No hay datos cargados para la busqueda")
            else:
                inf_rating(v)
        elif opcion == 4:
            if not v:
                print("❌ No se pudo crear la matriz, el arreglo esta vacio")
            else:
                matriz = matr(v)
        elif opcion == 5:
            pub_decadas(v)
        elif opcion == 6:
            if matriz is not None:
                generar_archivo(matriz, NAME)
            else:
                print("❌ La matriz no fue generada")
        elif opcion == 7:
            mostrar_archivo(NAME)
        else:
            print("❌ Opcion no valida!")


if __name__ == "__main__":
    principal()
