"""# Caracter es vocal?

def es_vocal(i):
    if i in "aeiouAEIOUÁÉÍÓÚáéíóú":
        return True
    return False


# Es un digito?

def es_digito(i):
    if i in "0123456789":
        return True
    return False


# Es blanco o punto?

def car_terminador(i):
    if i in " .":
        return True
    return False


# Es una consonante?


def es_consonante(i):
    if i in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ":
        return True
    return False
"""

def es_vocal(car):
    if car in 'aeiouAEIOU':
        return True
    else:
        return False


def es_consonante(car):
    ret = False
    if (car >= 'a' and car <= 'z') or (car >= 'A' and car <= 'Z'):
        if es_vocal(car) == False:
            ret = True
    return ret


def calcular_porcentaje(cant, total):
    if total == 0:
        return 0
    else:
        return cant * 100 / total


def principal():
    # Datos
    print('PROCESAMIENTO DE TEXTO')
    texto = input('Ingrese texto: ')
    # Proceso
    vocales = letras_pal = 0
    segunda_cons = False
    palabras_3voc4let = 0
    menor_long_segunda_cons = -1
    anterior = ''
    palabras_vpna = 0
    empieza_pv = False
    tiene_ga = False
    palabras_ga = 0
    total_palabras = 0
    for car in texto:
        if car == ' ' or car == '.':
            # Cuento todas las palabras del texto
            if letras_pal > 0:
                total_palabras += 1
            # Por lo menos 3 vocales y más de 4 letras
            if vocales >= 3 and letras_pal > 4:
                palabras_3voc4let += 1
            # Tenia consonante en la segunda posicion?
            if segunda_cons:
                # Es la más corta?
                if menor_long_segunda_cons == -1:
                    menor_long_segunda_cons = letras_pal
                elif letras_pal < menor_long_segunda_cons:
                    menor_long_segunda_cons = letras_pal
            # Termina con "n" o con "a"? Comienza con "p" o "v"?
            if anterior == 'n' or anterior == 'a' or anterior == 'N' or anterior == 'A':
                if empieza_pv:
                    palabras_vpna += 1
            # Tiene "ga"? La cuento
            if tiene_ga:
                palabras_ga += 1
            # Reiniciar variables de palabra
            vocales = letras_pal = 0
            segunda_cons = False
            empieza_pv = False
            tiene_ga = False
        else:
            # Contar letras/caracteres (longitud)
            letras_pal += 1
            # Contar vocales
            if es_vocal(car):
                vocales += 1
            # Detectar consonante en la 2da posicion
            if es_consonante(car) and letras_pal == 2:
                segunda_cons = True
            # Comienza con "p" o "v"?
            if (car in 'p' or car == 'P' or car == 'v' or car == 'V') and letras_pal == 1:
                empieza_pv = True
            # Tiene "ga"?
            if (car == 'a' or car == 'A') and (anterior == 'g' or anterior == 'G'):
                tiene_ga = True
        anterior = car

    # Resultados
    print('Palabras tenían por lo menos tres vocales y más de cuatro letras:', palabras_3voc4let)
    if menor_long_segunda_cons != -1:
        print('Longitud de la palabra más corta de entre las que contenían una consonante en la segunda posición: ',
              menor_long_segunda_cons)
    else:
        print('No había palabras con consonante en la segunda posición')
    print('Palabras que empiezan con "v" o con "p" y terminan con "n" o con "a":', palabras_vpna)
    porcentaje = calcular_porcentaje(palabras_ga, total_palabras)
    print('Porcentaje de palabras con la expresión "ga" sobre el total de palabras del texto:', porcentaje,'%')


if __name__ == '__main__':
    principal()