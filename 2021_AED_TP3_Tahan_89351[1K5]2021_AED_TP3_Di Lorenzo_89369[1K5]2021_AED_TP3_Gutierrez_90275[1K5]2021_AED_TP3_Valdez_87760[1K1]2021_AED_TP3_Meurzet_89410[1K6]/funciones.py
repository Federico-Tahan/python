import random


class Libro:
    def __init__(self, isbn, titulo, genero, idioma, precio):
        self.isbn = isbn
        self.tit = titulo
        self.gen = genero
        self.idm = idioma
        self.pre = precio


def conv_gen(gen):
    if gen == 0:
        gen = "Autoayuda"
    elif gen == 1:
        gen = "Arte"
    elif gen == 2:
        gen = "Ficción"
    elif gen == 3:
        gen = "Computación"
    elif gen == 4:
        gen = "Economía"
    elif gen == 5:
        gen = "Escolar"
    elif gen == 6:
        gen = "Sociedad"
    elif gen == 7:
        gen = "Gastronomía"
    elif gen == 8:
        gen = "Infantil"
    elif gen == 9:
        gen = "Otros"

    return gen


def conv_idm(idm):
    if idm == 1:
        idm = "Español"
    elif idm == 2:
        idm = "Inglés"
    elif idm == 3:
        idm = "Francés"
    elif idm == 4:
        idm = "Italiano"
    elif idm == 5:
        idm = "Otros"
    else:
        idm = "Idioma no valido"

    return idm


def to_string_titulo():
    return '{:<71}{:<39}{:<33}{:<26}{:<25}'.format('Titulo', 'ISBN', 'Genero',
                                                   'Idioma', 'Precio')


def to_string_libro(v):
    cad = "Titulo: {:<60} | ISBN: {:<30} | Genero: {:<22} | Idioma: {:<15} | Precio $ {:>10} |"
    return cad.format(v.tit, v.isbn, conv_gen(v.gen), conv_idm(v.idm), v.pre)


def digito(i):
    if i in "0123456789":
        return True

    return False


def validad_isbn():
    valido = False
    while valido is False:
        isbn = input("► Ingrese el codigo de identificacion o ISBN:")
        guion = 0
        ant = None
        guion_mal = False
        v = []
        for i in isbn:
            if digito(i):
                a = int(i)
                v.append(a)
        tam_v = len(v)
        if tam_v != 10:
            print("❌ Faltan numeros")
        else:
            n_1 = v[0]
            n_2 = v[1]
            n_3 = v[2]
            n_4 = v[3]
            n_5 = v[4]
            n_6 = v[5]
            n_7 = v[6]
            n_8 = v[7]
            n_9 = v[8]
            n_10 = v[9]
            numero = (10 * n_1) + (9 * n_2) + (8 * n_3) + (7 * n_4) + (6 * n_5) + (5 * n_6) + (4 * n_7) + (3 * n_8) + (
                    2 * n_9) + n_10

            if numero % 11 != 0:
                print("❌ El isbn ingresado no es divisible por 11")
            else:
                for i in isbn:
                    if i == "-":
                        guion += 1

                    if isbn[0] == "-":
                        guion_mal = True
                    elif isbn[-1] == "-":
                        guion_mal = True
                    elif ant == "-" and i == "-":
                        guion_mal = True
                    ant = i

                if guion != 3 or guion_mal:
                    print("❌ El isbn ingresado no es valido!")
                    valido = False
                else:
                    valido = True
                    return isbn


def register(v, n):
    cont = 1
    for i in range(n):
        print("► Ingrese los datos del libro N°", cont)
        cont += 1
        isbn = validad_isbn()
        nomb = input("► Ingrese el titulo del libro: ")
        while linear_search(v, nomb) != -1:
            nomb = input("► Ingrese el titulo del libro: ")
        genero = int(input(
            "► Ingrese el género del libro(0:Autoayuda,1:Arte,2:Ficción,3:Computación,4:Economía,5:Escolar,6:Sociedad,"
            "7:Gastronomía,8:Infantil,9:Otros): "))
        idioma = int(input("► Ingrese el Idioma (1:español,2:inglés,3:francés,4:italiano,5:otros): "))
        precio = int(input("► Ingrese el precio del libro: $"))
        v.append(Libro(isbn, nomb, genero, idioma, precio))
    print("✔ Carga completada.")
    return v


def generar_isbn():
    numero = -1
    n_1 = n_2 = n_3 = n_4 = n_5 = n_6 = n_7 = n_8 = n_9 = n_10 = 0
    while numero % 11 != 0:
        n_1 = random.randint(0, 9)
        n_2 = random.randint(0, 9)
        n_3 = random.randint(0, 9)
        n_4 = random.randint(0, 9)
        n_5 = random.randint(0, 9)
        n_6 = random.randint(0, 9)
        n_7 = random.randint(0, 9)
        n_8 = random.randint(0, 9)
        n_9 = random.randint(0, 9)
        n_10 = random.randint(0, 9)

        numero = (10 * n_1) + (9 * n_2) + (8 * n_3) + (7 * n_4) + (6 * n_5) + (5 * n_6) + (4 * n_7) + (3 * n_8) + (
                2 * n_9) + n_10

    n_1 = str(n_1)
    n_2 = str(n_2)
    n_3 = str(n_3)
    n_4 = str(n_4)
    n_5 = str(n_5)
    n_6 = str(n_6)
    n_7 = str(n_7)
    n_8 = str(n_8)
    n_9 = str(n_9)
    n_10 = str(n_10)
    isbn = n_1 + n_2 + "-" + n_3 + n_4 + n_5 + "-" + n_6 + n_7 + n_8 + "-" + n_9 + n_10
    return isbn


def linear_search(v, x):
    n = len(v)
    for i in range(n):
        if x == v[i].tit:
            return i
    return -1


def register_auto(v, n):
    nombres = (
        "Poema de Gilgamesh", "Libro de Job (de la Biblia)", "Las mil y una noches", "Saga de Njál",
        "Todo se desmorona",
        "Cuentos infantiles", "Divina Comedia", "Orgullo y prejuicio", "Papá Goriot", "Molloy, Malone muere",
        "Decamerón", "Ficciones", "Cumbres Borrascosas", "El extranjero", "Poemas", "Viaje al fin de la noche",
        "Don Quijote de la Mancha", "Los cuentos de Canterbury", "Relatos cortos", "Nostromo", "Grandes Esperanzas",
        "Jacques el fatalista", "Berlin Alexanderplatz", "Crimen y castigo", "El idiota", "Los endemoniados",
        "Los hermanos Karamazov", "Middlemarch", "El hombre invisible", "Medea", "¡Absalom, Absalom!",
        "El ruido y la furia",
        "Madame Bovary", "La educación sentimental", "Romancero gitano", "Cien años de soledad",
        "El amor en los tiempos del cólera",
        "Fausto", "Almas muertas", "El tambor de hojalata", "Gran Sertón: Veredas", "Hambre", "El viejo y el mar",
        "Ilíada", "Odisea", "Casa de muñecas", "Ulises", "Relatos cortos", "El proceso", "El castillo", "Shakuntala",
        "El sonido de la montaña", "Zorba, el griego", "Hijos y amantes", "Gente independiente", "Poemas 2",
        "El cuaderno dorado", "Pippi Calzaslargas", "Diario de un loco", "Hijos de nuestro barrio", "Los Buddenbrook",
        "La montaña mágica", "Moby-Dick", "Ensayos", "La historia", "Beloved", "Genji Monogatari",
        "El hombre sin atributos",
        "Lolita", "1984", "Las metamorfosis", "Libro del desasosiego", "Cuentos", "En busca del tiempo perdido",
        "Gargantúa y Pantagruel", "Pedro Páramo", "Masnavi", "Hijos de la medianoche", "Bostan",
        "Tiempo de migrar al norte",
        "Ensayo sobre la ceguera", "Hamlet", "El rey Lear", "Otelo", "Edipo rey", "Rojo y negro",
        "Vida y opiniones del caballero Tristram Shandy",
        "La conciencia de Zeno", "Los viajes de Gulliver", "Guerra y paz", "Ana Karenina", "La muerte de Iván Ilich",
        "Las aventuras de Huckleberry Finn", "Ramayana", "Eneida", "Mahabhárata", "Hojas de hierba",
        "La señora Dalloway",
        "Al faro", "Memorias de Adriano")
    for i in range(n):
        isbn = generar_isbn()
        nomb = random.choice(nombres)
        while linear_search(v, nomb) != -1:
            nomb = random.choice(nombres)
        gen = random.randint(0, 9)
        idioma = random.randint(1, 5)
        precio = random.randint(120, 16000)

        v.append(Libro(isbn, nomb, gen, idioma, precio))
    print("\n✔ Datos generados correctamente.")
    return v


def search_may(arreglo):
    ind_may = None
    n = len(arreglo)
    mayor = arreglo[0]
    for x in range(n):
        if arreglo[x] > mayor:
            mayor = arreglo[x]
            ind_may = x

    return [mayor, ind_may]


def ordenar_libros(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].tit > v[j].tit:
                v[i], v[j] = v[j], v[i]


def libros_por_genero(vector):
    vector_conteo = [0] * 10
    for i in range(len(vector)):
        if vector[i].gen == 0:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 1:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 2:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 3:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 4:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 5:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 6:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 7:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 8:
            vector_conteo[vector[i].gen] += 1
        elif vector[i].gen == 9:
            vector_conteo[vector[i].gen] += 1

    return vector_conteo


def to_string_libros_gen(i, vc):
    cad = "Genero: {:<15} | Libros: {:<10}"
    return cad.format(conv_gen(i), vc[i])


def mostrar_libros_genero(vc):
    print("📗 La cantidad de libros por genero es:")
    for i in range(len(vc)):
        print(to_string_libros_gen(i, vc))


def ordenar_precios(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].pre < v[j].pre:
                v[i], v[j] = v[j], v[i]
    return v


def gen_popular(array):
    v = search_may(array)
    genero = v[1]
    cantidad = v[0]

    return [genero, cantidad]


def search_isbn(vector, isbn):
    n = len(vector)
    indice = None
    for i in range(n):
        if vector[i].isbn == isbn:
            indice = i

    return indice


def mostrar_libro(arreglo):
    cad = "Titulo: {:<60} | ISBN: {:<30} | Genero: {:>22} | Idioma: {:>15} | Precio: {:>10} |"
    return cad.format(arreglo.tit, arreglo.isbn, conv_gen(arreglo.gen), conv_idm(arreglo.idm), arreglo.pre)


def suma_precios(vector):
    n = len(vector)
    total_precio = 0
    for i in range(n):
        total_precio += vector[i].pre

    return total_precio


def libros_solicitados(isbn, vector):
    libros_soli = []
    while isbn != "0":
        a = search_isbn(vector, isbn)
        if a is not None:
            b = vector[a]
            libros_soli.append(b)
        else:
            print("❌ El libro", isbn, "no esta disponible")
        isbn = input("► Ingrese el codigo de idenficiacion (finaliza la carga con 0): ")

    return libros_soli


def agrupar_genero(vector, gen):
    n = len(vector)
    gen_v = []
    for i in range(n):
        if vector[i].gen == gen:
            gen_v.append(vector[i])

    return gen_v


def agrupar_idioma(vector, idm):
    n = len(vector)
    idm_v = []
    for i in range(n):
        if vector[i].idm == idm:
            idm_v.append(vector[i])

    return idm_v


def mostrar_vector(v):
    print(to_string_titulo())
    for reg in v:
        print(to_string_libro(reg))

