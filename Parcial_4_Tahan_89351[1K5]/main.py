"""Una fábrica de bicicletas desea un programa para procesar los datos de los bicicletas que fabrica. Para cada bicicleta
se registran los siguientes datos: código de identificación (un entero), nombre del modelo (una cadena),
precio, tipo de bicicleta (un valor entre 0 y 9 por ejemplo: 0: de paseo, 1: de competición, etc.)
y tamaño del rodado (un valor entre 0 y 4 por ejemplo: 0: para niños, 1: rodado medio, etc.).
 Se pide definir un tipo registro Bicicleta con los campos que se indicaron, y un programa completo
 con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Bicicleta en un arreglo de registros (cargue n por teclado). Puede cargar
los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y
si la hace automática entonces TODA debe ser automática). Valide los campos que sean necesarios. El arreglo debe crearse
de forma que siempre quede ordenado de mayor a menor, según el precio de las bicicletas, y para hacer esto debe aplicar
el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la solución basada en
cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el vector completo a razón de un registro por línea, pero muestre solo los registros cuyo precio sea mayor a
p (cargue p por teclado) y que sean del tipo 0.

3- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del modelo sea igual a nom (cargar nom por
teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un mensaje. La
búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

4- A partir del arreglo creado en el punto 1, crear un archivo de registros en el cual se copien los datos de todos los
registros cuyo tamaño de rodado no sea ni 0 ni 1.

5- Mostrar los registros del archivo que se creó en el punto 4. Mostrar a razón de un registro por línea en la pantalla
, y al final de listado muestre dos líneas adicionales: una indicando la cantidad de registros que se mostraron, y
la otra indicando el precio promedio de todos los registros que se mostraron."""

#Iden entero
#moledlo
#precio
#tipo 0 -9
#rodado 0 - 4

from funciones import *


def principal():
    v = []
    AR = "bici.pydb"
    opcion = None

    while opcion != 6:
        print("=" * 30)
        print("\tFabrica de bicicletas")
        print("=" * 30)
        print()
        print("1-Cargar registros")
        print("2-Mostrar registros")
        print("3-Buscar registro")
        print("4-Grabar registro")
        print("5-Mostrar registro")
        print("6 Finalizar Programa")
        print()

        opcion = int(input("Ingrese la opcion: "))

        if opcion == 1:
            n = int(input("Ingrese la cantidad de registros que desee registrar: "))
            cargar_arreglo_ordenado(v, n)
        elif opcion == 2:
            if not v:
                print("No se encontraron datos.")
            else:
                p = int(input("Ingrese un precio a superar para la muestra de registros: "))
                mostrar_vector(v, p)
        elif opcion == 3:
            if not v:
                print("No se encontraron datos ")
            else:
                nom = input("Ingrese el modelo de registro a buscar: ")
                op3 = busqueda_sec(v, nom)
                if op3 is None:
                    print("No se encontraron registros con ese modelo.")
                else:
                    print(to_string(v[op3]))
        elif opcion == 4:
            crear_archivo(v, AR)
        elif opcion == 5:
            mostrar_archivo(AR)
        elif opcion == 6:
            print("Programa Finalizado.")
        else:
            print("Opión no valida")


if __name__ == "__main__":
    principal()
