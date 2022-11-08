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


class Treking:
    def __init__(self, dia, descripcion, precio, personas, guia):
        self.day = dia
        self.desc = descripcion
        self.price = precio
        self.people = personas
        self.guia = guia


def validacion_dia(vt):
    while vt > 31 or vt < 0:
        print("Dia incorrecto.")
        vt = int(input("Ingrese el dia (1 al 31): "))

    return vt


def validacion_importe(importe):
    while importe < 0:
        print("El importe debe ser mayor a 0")
        importe = int(input("Ingrese el importe (mayor a 0): "))

    return importe


def validacion_personas(p):
    while p < 0:
        print("Cantidad de personas inconrrecta.")
        p = int(input("Ingrese la cantidad de personas (0 o mayor a 0): "))

    return p


def registro(v):
    n = int(input("Ingrese el número de actividades que desee registrar: "))

    for i in range(1, n + 1):
        print("Ingrese los datos del Servicio N°", i)
        dia = validacion_dia(int(input("Ingrese el dia (1 al 31): ")))
        descripcion = input("Ingrese la descripcion: ")
        importe = validacion_importe((float(input("Ingrese el importe (mayor a 0):"))))
        cant_people = validacion_personas(int(input("Ingrese la cantidad de personas (0 o mayor a 0): ")))
        name_guia = input("Ingrese el nombre del guia: ")
        v.append(Treking(dia, descripcion, importe, cant_people, name_guia))
    print("✔ Carga completada.")

    return v


def write(v):
    n = len(v)
    for i in range(n):
        print("-Identificador:", v[i].day, "-Descripción:", v[i].desc, "-Precio: $", v[i].price,
              "-cantidad de personas:", v[i].people, "-Nombre del guia:", v[i].guia)


def ordenar_dia(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].day > v[j].day:
                v[i], v[j] = v[j], v[i]
    return v


def ini_fin(v):
    n = len(v)
    v_day = []
    ini = int(input("Ingrese el dia de partida entre: "))
    fin = int(input("Ingrese el dia de partida hasta: "))
    cant_personas = 0

    for i in range(n):
        if ini <= v[i].day <= fin:
            v_day.append(v[i])
            cant_personas += v[i].people

    if not v_day:
        print("No hay actividades en este rango de dias")
    else:
        ordenar_dia(v_day)
        write(v_day)
        print("La cantidad de personas que participaran en las actividades son:", cant_personas)


def punto3(actividades):
    n = len(actividades)
    acumulador = [0] * 31

    for i in range(n):
        acumulador[actividades[i].day - 1] += actividades[i].price

    for i in range(31):
        if acumulador[i] > 0:
            print("Dia", i + 1, ":", acumulador[i])




def ordenar_por_personas(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].people < v[j].people:
                v[i], v[j] = v[j], v[i]
    return v[0]


def to_string(v):
    cad = "Dia: {:>60} | Descripcion: {:<30} |"
    return cad.format(v.day, v.desc)


def buscar_dia(v):
    n = len(v)
    a = ordenar_por_personas(v)
    x = int(input("Ingrese la cantidad de dias a superar: "))

    write(a[0])
    if a[0].people > x:
        print("Se necesitara un guia extra para cada actividad")


def buscar_v(v):
    d = int(input("Ingrese el dia a buscar: "))
    p = input("Ingrese la descripcion a buscar: ")

    n = len(v)

    for i in range(n):
        if v[i].day == d and v[i].desc == p:
            return i


def writeesp(v):
    print()
    print("-Identificador:", v.day, "-Descripción:", v.desc, "-Precio: $", v.price,
          "-cantidad de personas:", v.people, "-Nombre del guia:", v.guia)

