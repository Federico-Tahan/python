"""1- Cargar el arreglo pedido con los datos de las n actividades. Valide que el día sea mayor o igual a 1 y menor o igual a 31,
que el importe a cobrar sea mayor a cero, y que la cantidad de personas sea 0 o mayor que 0. Puede hacer la carga en forma manual,
o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos
una debe programar.

2- Mostrar todos los datos de las actividades, a razón de un registro por línea, que tengan día de partida entre ini y fin,
siendo ini y fin valores enteros que se cargan por teclado. El listado debe salir ordenado por día de partida. Al final del
listado, mostrar una línea adicional con la cantidad total de personas que participarán las actividades mostradas en el listado.

3- Determinar y mostrar el importe total recaudado por cada posible día del mes. En total, 31 acumuladores. Mostrar todos los
valores cuyo resultado sea mayor a 0.

4- Determinar y mostrar el día y la descripción de la actividad que tenga más personas registradas. Si además esa actividad
supera una cantidad x (x se carga por teclado) informar con otro mensaje que hará falta un guía extra. En el caso de que exista
más de una actividad con la misma cantidad de másxima personas mostrar todas, y para cada una informar (si corresponde) el mensaje
para el guía extra.

5- Determinar si existe una actividad para el día d y con descripción t, siendo d y t valores que se carga por teclado. Si exsite,
mostrar todos sus datos. Si no existe, indicar con un mensaje. Si existe más de una actividad para el día y descripción cargados
mostrar solo la primera."""

from funciones import *


def principal():
    v = []
    opcion = None

    while opcion != 6:
        print("=" * 30)
        print("\tMenú de opciones")
        print("=" * 30)
        print()
        print("1-Registrar Actividades")
        print("2-Mostrar Actividades")
        print("3-Mostrar importe recaudado por dia")
        print("4-Buscar dia con la misma descripcion con mas personas")
        print("5 Buscar actividad-")
        print("6 Finalizar programa-")
        print()

        opcion = int(input("Ingrese la opcion: "))

        if opcion == 1:
            registro(v)
        elif opcion == 2:
            if not v:
                print("No se encontraron registros ")
            else:
                ini_fin(v)
        elif opcion == 3:
            if not v:
                print("No se encontraron registros ")
            else:
                punto3(v)
        elif opcion == 4:
            if not v:
                print("No se encontraron registros ")
            else:
                buscar_dia(v)
        elif opcion == 5:
            if not v:
                print("No se encontraron registros")
            else:
                a = buscar_v(v)
                if a is None:
                    print("No existe datos para esta actividad")
                else:
                    writeesp(v[a])
        elif opcion == 6:
            print("Programa Finalizado.")
        else:
            print("Opión no valida")


if __name__ == "__main__":
    principal()