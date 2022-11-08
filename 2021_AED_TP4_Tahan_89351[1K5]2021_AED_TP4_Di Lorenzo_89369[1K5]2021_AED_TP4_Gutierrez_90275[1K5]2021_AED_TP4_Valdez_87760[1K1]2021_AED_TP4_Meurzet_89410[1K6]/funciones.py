import os
import pickle


class Libreria:
    def __init__(self, titulo, revisiones, year, idioma, rating, isbn):
        self.titulo = titulo
        self.rev = revisiones
        self.year = year
        self.idioma = idioma
        self.rating = rating
        self.isbn = isbn


def quitar_salto_de_linea(a):
    a = a[:-1]

    return a


def str_libreria(line):
    token = line.split(",")
    titulo = token[0]
    revisiones = int(token[1])
    year = int(token[2])
    idioma = int(token[3])
    rating = float(token[4])
    isbn = quitar_salto_de_linea(token[5])
    libreria = Libreria(titulo, revisiones, year, idioma, rating, isbn)
    return libreria


def sub_menu(a):
    while a != 1 and a != 2 and a != 3:
        print("❌ Opcion no valida.")
        a = int(input("➡ Ingrese la forma de busqueda:"))

    return a


def add_in_orden_b(v, lib):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].isbn == lib.isbn:
            pos = c
            break

        if lib.isbn < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [lib]


def to_string_libro(v):
    cad = "Revisiones: {:<25} | ISBN: {:<30} | Año: {:<20} | Idioma: {:<20} | Rating {:<20} | Titulo: {:<10} "
    return cad.format(v.rev, v.isbn, v.year, v.idioma, v.rating, v.titulo)


def mostrar_vector(v):
    print(to_string_libro(v))


def buscar_isbn(p):
    if len(p) == 0:
        print("❌ No hay datos cargados")
        print()
        return

    x = input("➡ Ingrese el ISBN a buscar:")

    n = len(p)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if p[c].isbn == x:
            print("✔ Libro encontrado")
            mostrar_vector(p[c])
            p[c].rev = p[c].rev + 1
            print()
            return

        if x < p[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    print("❌ No hay un Libro registrado con ese número de ISBN")
    print()


def buscar_titulo(v):
    pos = None
    titulo = input("➡ Ingrese el titulo a buscar: ")
    for i in range(len(v)):
        if titulo == v[i].titulo:
            return i

    return pos


def search_book(v):
    print("1- Busqueda por ISBN")
    print("2- Busqueda por Titulo")
    print("3- Volver")
    opcion = sub_menu(int(input("➡ Ingrese la forma de busqueda:")))

    if opcion == 1:
        buscar_isbn(v)

    elif opcion == 2:
        pos = buscar_titulo(v)
        if pos is None:
            print("❌ No se encontro el libro")
        else:
            mostrar_vector(v[pos])
            v[pos].rev = v[pos].rev + 1


def search_may(arreglo):
    ind_may = None
    n = len(arreglo)
    mayor = arreglo[0].rev
    for x in range(n):
        if arreglo[x].rev > mayor:
            mayor = arreglo[x].rev
            ind_may = x
    return ind_may


def inf_rating(arreglo):
    cont = rating_tot = 0
    ind = search_may(arreglo)
    n = len(arreglo)

    for i in range(n):
        if arreglo[ind].idioma == arreglo[i].idioma:
            cont += 1
            rating_tot += arreglo[i].rating

    promedio = rating_tot / cont

    if arreglo[ind].rating == promedio:
        print("📕 El rating del libro con mayor revisiones es igual al rating promedio 📘")
    elif arreglo[ind].rating > promedio:
        print("📕 El rating del libro con mayor revisiones es mayor al rating promedio 📘")
    elif arreglo[ind].rating < promedio:
        print("📕 El rating del libro con mayor revisiones es menor al rating promedio 📘")


def dec_may(arreglo):
    ind_may = None
    n = len(arreglo)
    mayor = arreglo[0]
    for x in range(n):
        if arreglo[x] > mayor:
            mayor = arreglo[x]
            ind_may = x

    print("📕 La decada con mayor cantidad de libros publicados fue la", ind_may, "con", mayor, "publicaciones 📘")


def obtener_decada(fecha):
    ind = None

    if fecha == 2000:
        return 9
    elif 1900 <= fecha <= 1999:
        decada = fecha - 1900
        ind = decada // 10
        return ind


def pub_decadas(vector):
    c = [0] * 10

    n = len(vector)
    for i in range(n):
        ind = obtener_decada(vector[i].year)
        if ind is not None:
            c[ind] += 1

    print("Cantidad de servicios tipo:")
    for r in range(10):
        if c[r] != 0:
            print("📘Decada", r, "Cantidad de libros publicados:", c[r])

    dec_may(c)


def matr(arreglo):
    mat = [[0] * 21 for i in range(27)]
    cont = 0

    for lib in arreglo:
        if 2000 <= lib.year <= 2020:
            f = lib.idioma - 1
            c = lib.year - 2000
            mat[f][c] = lib

    return mat



def generar_archivo(mat, name):
    cont = 0
    arch = open(name, "wb")
    for i in range(27):
        for x in range(20):
            if mat[i][x] != 0:
                pickle.dump(mat[i][x], arch)
                cont += 1
    arch.close()
    print("✔ El archivo fue creado con exito!")
    print("📘 Se Grabaron", cont, "Registros")


def mostrar_archivo(FD):
    if not os.path.exists(FD):
        print('❌ El archivo', FD, 'no existe')
        print()
        return

    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        pac = pickle.load(m)
        print(to_string_libro(pac))

    m.close()
    print()
