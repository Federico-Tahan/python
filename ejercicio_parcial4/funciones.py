import os
import pickle
import random


class Celulares:
    def __init__(self, numero, titular, plan, min, prov):
        self.numero = numero
        self.titular = titular
        self.plan = plan
        self.minutos = min
        self.provincia = prov


NOMBRES = ['Nico', 'Andy', 'Lucas', 'Juan', 'Jere', 'Rafa', 'Pablo', 'Lautaro', 'Rodrigo', 'Romi', 'Sole', 'Euge',
           'Lauri', 'Tati', 'Sabri', 'Cande', 'Cami']
APELLIDOS = ['Steffo', 'Martinez', 'Peralta', 'Morinigo', 'Gasquez', 'Zavalía', 'Giannetto', 'Conforti', 'Brito',
             'Lopez']


def validar_mayor(lim):
    n = lim - 1
    while n <= lim:
        n = int(input('Valor mayor a ' + str(lim) + ' por favor: '))
        if n <= lim:
            print('\t\tError. Se pidió mayor a', lim, 'cargue de nuevo.')
    return n


def to_string(reg):
    return 'Numero: ' + str(reg.numero) + \
           ' | Titular: ' + reg.titular + \
           ' | Plan: ' + str(reg.plan) + \
           ' | Minutos: ' + str(reg.minutos) + \
           ' | Provincia: ' + str(reg.provincia)


def mostrar_string(a):
    print("Mostrando registros...")
    for i in range(len(a)):
        print(to_string(a[i]))


def validar_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup) + ' por favor: '))
        if n < inf or n > sup:
            print('\t\tError. Se pidió entre', inf, 'y', sup, 'cargue de nuevo,')
    return n


def add_in_orden_b(p, celular):
    n = len(p)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if p[c].numero == celular.numero:
            pos = c
            break

        if celular.numero < p[c].numero:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    p[pos:pos] = [celular]


def generar_arreglo(v, n):
    for i in range(n):
        numero = random.randint(1000000000, 9999999999)
        provincia = random.randint(1, 23)
        plan = random.randint(0, 19)
        minutos = random.randint(1, 999)
        titular = random.choice(NOMBRES) + " " + random.choice(APELLIDOS)

        celular = Celulares(numero, titular, plan, minutos, provincia)
        add_in_orden_b(v, celular)

    print("Carga completa.")


def crear_archivo(p, FD, min):
    print('Grabando todos los datos en el archivo', FD, '...')
    m = open(FD, 'wb')
    for celular in p:
        if celular.minutos > min:
            pickle.dump(celular, m)
    m.close()
    print('Listo')
    print()


def mostrar_archivo(FD, y):
    cont_tot = 0
    cont_plan = 0
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe')
        print()
        return

    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        pac = pickle.load(m)
        cont_tot += 1
        if pac.plan == y:
            cont_plan += 1
        print(to_string(pac))

    m.close()
    por(cont_plan, cont_tot, y)


def por(a, b, y):
    represent = (a / b) * 100
    print("Los planes", y, "representan un ", round(represent, 2), "% del total del archivo", sep="")


def generate_mat_cont(vec):
    cant = [[0] * 20 for f in range(23)]

    for cel in vec:
        f = cel.provincia - 1
        c = cel.plan
        cant[f][c] += cel.minutos

    print('Matriz de conteo generada')
    return cant


def mostrar_matriz(matriz):
    cad = 'Para el plan {} en la provincia {} se consumieron {} minutos'
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] != 0:
                print(cad.format(f+1, c, matriz[f][c]))


def buscar_men_min(matriz):
