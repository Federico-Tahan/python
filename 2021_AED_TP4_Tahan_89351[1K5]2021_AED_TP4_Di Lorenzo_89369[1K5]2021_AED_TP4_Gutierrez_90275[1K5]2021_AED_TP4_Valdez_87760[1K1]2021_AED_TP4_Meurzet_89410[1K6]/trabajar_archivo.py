import os.path
from funciones import *

ARCHIVO = "libros.csv"


def generar_arreglo(v):
    cont = 0

    if os.path.exists(ARCHIVO):
        arch = open("libros.csv", mode="rt", encoding="utf8")
        for line in arch:
            cont += 1
            if cont > 1:
                libreria = str_libreria(line)
                add_in_orden_b(v, libreria)
        arch.close()

    return v
