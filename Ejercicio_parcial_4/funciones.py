__author__ = 'Algoritmos y Estructuras de Datos'

import random


def validar_mayor_que(minimo, mensaje='Ingrese un numero: '):
    numero = minimo
    while numero <= minimo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print('Error!!!! El valor ingresado debe ser mayor a {}'.format(minimo))
    return numero


def validar_rango(minimo, maximo, mensaje='Ingrese un numero: '):
    numero = minimo - 1
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print('Error!!!! El valor ingresado debe esta comprendido entre {} y {}'.format(minimo, maximo))
    return numero


class Venta:
    def __init__(self, cliente, tipo_venta, marca_auto, cuotas_pagas, monto_plan):
        self.cliente = cliente
        self.tipo_venta = tipo_venta
        self.marcar_auto = marca_auto
        self.cuotas_pagas = cuotas_pagas
        self.monto_plan = monto_plan


def to_string(venta):
    cad = '| {:<30} | {:^10} | {:^10} | {:>6} | {:>10.2f} |\n' \
          '{:<86}\n'
    return cad.format(venta.cliente, venta.tipo_venta, venta.marcar_auto, venta.cuotas_pagas, venta.monto_plan,
                      '=' * 91)


def add_in_orden_b(p, auto):
    n = len(p)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if p[c].cliente == auto.cliente:
            pos = c
            break

        if auto.cliente < p[c].cliente:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    p[pos:pos] = [auto]


def encabezado():
    cad = '{:<86}\n' \
          '| {:<30} | {:^10} | {:^10} | {:>6} | {:>10} |\n' \
          '{:<86}\n'
    return cad.format('=' * 91, 'Cliente', 'Tpo. Venta', 'Marca', 'Cuotas', 'Monto', '=' * 91)


def to_string_libro(v):
    cad = "Cliente:: {:<25} | Tipo de venta: {:<30} | Marca: {:<20} | Cuotas pagas: {:<20} | Monto del plan {:<20}"
    return cad.format(v.cliente, v.tipo_venta, v.marcar_auto, v.cuotas_pagas, v.monto_plan)


def mostrar_vector(v):
    print(encabezado())
    for i in range(len(v)):
        print(to_string(v[i]))


def cargar_vector(v):
    n = int(input("Ingrese la cantidad de ventas a procesar: "))

    for i in range(n):
        nombre = input("Ingrese el nombre del cliente: ")
        tipo = validar_rango(0, 3, "Ingrese el tipo de venta (0 - 3): ")
        marca = validar_rango(1, 15, "Ingrese la marca del auto (1-15): ")
        cuota = int(input("Ingrese la cantidad de cuotas pagas: "))
        monto = float(input("Ingrese el monto total del plan: "))
        auto = Venta(nombre, tipo, marca, cuota, monto)
        add_in_orden_b(v, auto)
    print("Carga completa..")
