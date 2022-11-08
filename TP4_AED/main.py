"w = escribir en el archivo pero no ver los datos del mismo"
"r = leer contendio del archivo"
"ej m1= open('paises.csv','r')"

from funciones import *


def principal():
    p = []
    c = None
    global FD
    FD = "viajes.doc"
    opcion = None

    while opcion != 6:
        print("=" * 30)
        print("\tMenú de opciones")
        print("=" * 30)
        print()
        print("1-Cargar arreglo")
        print("2-Procesamiento de números enteros")
        print("3-Salir del programa")
        print()

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            p = cargar_arreglo_ordenado(p)
        elif opcion == 2:
            v = len(p)
            if v == 0:
                print("Pibe el vector ta vacio, llenalo")
            else:
                name_chofer = input("Ingrese el nombre del chofer a determinar lo cobrado: ")
                total_cobrado = total_chofer(name_chofer, p)
                print("El total cobrado por", name_chofer, "fue:", total_cobrado)
        elif opcion == 3:
            c = viaje_servicio(p)
            mostrar_arreglo(c)
        elif opcion == 4:
            if c is None:
                print("El vector del punto 3 está vacio")
            else:
                crear_archivo(c)
        elif opcion == 5:
            pass
        elif opcion == 6:
            print("Programa Finalizado.")


if __name__ == "__main__":
    principal()
