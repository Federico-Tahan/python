import os
import pickle
import random


MARCAS = ["Bergamont", "Bianchi", "BMC", "Bottechia", "BTwin", "Bulls", "Canyon", "Colnago", "Coluer", "Commencal",
          "Corratec",
          "Cube", "Felt", "Focus", "Fuji", "Ghost", "GT", "Isaac", "Kemo", "Kona", "Kross", "KTM", "Kuota", "Lapierre",
          "Look",
          "Pinarello", "Radon", "Ridley", "Rose", "Stevens", "Univega", "Willier", "Van Rysel", "Cannondale", "Giant",
          "Scott",
          "Avanti", "Breezer", "Charge", "Colner", "Devinci", "DiamondBack", "Fezzari", "Fondriest", "Forme", "Ideal",
          "Jamis",
          "Moozes", "Norco", "Polygon", "Principia", "Raleigh", "RTS Carbon", "Trigon", "Vitus", "Vivelo", "Wheeler"]

# Iden entero
# moledlo
# precio
# tipo 0 -9
# rodado 0 - 4

class Bicicleta:
    def __init__(self, identificador, modelo, precio, tipo, rodado):
        self.idn = identificador
        self.modelo = modelo
        self.precio = precio
        self.tipo = tipo
        self.rodado = rodado


def add_in_orden_b(p, bici):
    n = len(p)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if p[c].precio == bici.precio:
            pos = c
            break

        if bici.precio > p[c].precio:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    p[pos:pos] = [bici]


def to_string(pac):
    r = ""
    r += "{:<25}".format("Identificador: " + str(pac.idn))
    r += "{:<30}".format("Modelo: " + str(pac.modelo))
    r += "{:<20}".format("Precio: " + str(pac.precio))
    r += "{:<30}".format("Tipo de bicicleta: " + str(pac.tipo))
    r += "{:<20}".format("Rodado: " + str(pac.rodado))
    return r


def mostrar_vector(v, p):
    cont = 0
    for i in range(len(v)):
        if v[i].precio > p and v[i].tipo == 0:
            cont += 1
            print(to_string(v[i]))
    if cont == 0:
        print("No hay datos del tipo 0 con un importe superior al ingresado.")


def cargar_arreglo_ordenado(v, n):
    for i in range(n):
        identificador = random.randint(100, 10000)
        modelo = random.choice(MARCAS)
        precio = random.randint(1000, 90000)
        tipos = random.randint(0, 9)
        rodado = random.randint(0, 4)
        bici = Bicicleta(identificador, modelo, precio, tipos, rodado)
        add_in_orden_b(v, bici)
    print("Datos cargados.")


def busqueda_sec(p, nom):
    n = len(p)
    pos = None
    for i in range(n):
        if nom == p[i].modelo:
            return i
    return pos


def crear_archivo(p, AR):
    if len(p) == 0:
        print("No hay datos cargados.")
        print()
        return

    print("Grabando todos los datos en el archivo", AR, "...")
    m = open(AR, "wb")
    for bici in p:
        if bici.rodado != 0 and bici.rodado != 1:
            pickle.dump(bici, m)

    m.close()
    print("Listo.")
    print()


def mostrar_archivo(AR):
    if not os.path.exists(AR):
        print("El archivo", AR, "no existe")
        print()
        return

    cont_reg = 0
    cont_precio = 0
    tbm = os.path.getsize(AR)
    m = open(AR, "rb")

    print("Contenido del archivo", AR, "...")

    while m.tell() < tbm:
        bici = pickle.load(m)
        cont_reg += 1
        cont_precio += bici.precio
        print(to_string(bici))

    m.close()
    print("La cantidad de registros mostrados fueron", cont_reg)
    prom = cont_precio / cont_reg
    print("El precio promedio de los registros mostrados fue de $", round(prom, 2), sep="")