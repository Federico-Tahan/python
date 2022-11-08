import pickle


class Transporte:
    def __init__(self, boleto, chofer_name, price, origen, destino, tipo):
        self.boleto = boleto
        self.chofer = chofer_name
        self.precio = price
        self.origen = origen
        self.destino = destino
        self.tipo = tipo


def add_in_orden_s(p, viajes):
    n = len(p)
    pos = n
    for i in range(n):
        if viajes.boleto < p[i].boleto:
            pos = i
            break

    p[pos:pos] = [viajes]


def validar_mayor(lim):
    n = lim - 1
    while n <= lim:
        n = int(input('Valor mayor a ' + str(lim) + ' por favor: '))
        if n <= lim:
            print('\t\tError. Se pidió mayor a', lim, 'cargue de nuevo.')
    return n


def validar_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup) + ' por favor: '))
        if n < inf or n > sup:
            print('\t\tError. Se pidió entre', inf, 'y', sup, 'cargue de nuevo,')
    return n


def cargar_arreglo_ordenado(p):
    print('Cantidad de viajes')
    n = validar_mayor(0)

    print()
    print('Ingrese los datos de los viajes')
    for i in range(n):
        print('Número de boleto')
        boleto = validar_mayor(0)

        print('Nombre del chofer')
        nom = input('Nombre: ')

        print('Costo del boleto')
        precio = validar_mayor(0)

        print('Seleccione el origen del viaje:\n'
              '1-\n'
              '2-\n'
              '3-\n'
              '4-\n'
              '5-\n'
              '6-\n'
              '7-\n'
              '8-\n'
              '9-\n'
              '10-\n')
        origen = validar_intervalo(0, 10)

        print('Seleccione el destino del viaje:\n'
              '1-\n '
              '2-\n'
              '3-\n'
              '4-\n'
              '5-\n'
              '6-\n'
              '7-\n'
              '8-\n'
              '9-\n'
              '10-\n')
        destino = validar_intervalo(0, 10)

        print('Seleccione el tipo de servicio:\n'
              '1-\n'
              '2-\n'
              '3-\n'
              '4-\n'
              '5-\n')
        tipo = validar_intervalo(0, 5)

        transporte = Transporte(boleto, nom, precio, origen, destino, tipo)
        add_in_orden_s(p, transporte)
        print()

    return p


def total_chofer(name, vector):
    total = 0

    for i in vector:
        if i.chofer == name:
            total += i.precio

    return total


def viaje_servicio(p):
    c = []
    print('Seleccione el tipo de servicio:\n'
          '1-\n'
          '2-\n'
          '3-\n'
          '4-\n'
          '5-\n')
    tipo = validar_intervalo(0, 5)

    for i in p:
        if tipo == i.tipo:
            c.append(i)

    return c


def to_string(via):
    r = ''
    r += '{:<25}'.format('Numero de boleto: ' + str(via.boleto))
    r += '{:<30}'.format('Nombre del chofer: ' + via.chofer)
    r += '{:<30}'.format('Precio del boleto: ' + str(via.precio))
    r += '{:<20}'.format('Origen: ' + str(via.origen))
    r += '{:<20}'.format('Destino: ' + str(via.destino))
    r += '{:<20}'.format('Tipo de servicio: ' + str(via.tipo))
    return r


def mostrar_arreglo(c, mensaje='Contenido:'):
    if len(c) == 0:
        print('No hay datos cargados')
        print()
        return

    print(mensaje)
    for viaje in c:
        print(to_string(viaje))

    print()


def crear_archivo(c):
    global FD
    FD = "viajes.doc"
    if len(c) == 0:
        print('No hay datos cargados')
        print()
        return

    print('Grabando todos los datos en el archivo', FD, '...')
    m = open(FD, 'wb')
    for paciente in c:
        pickle.dump(paciente, m)

    m.close()
    print('Listo')
    print()

