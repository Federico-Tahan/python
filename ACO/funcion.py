"""def hexadecimal(cociente_hexa):
    cont = 0
    ant = num = ""
    resultado = ""
    resto_hexa = cociente_hexa
    # HEXADECIMAL

    res_st = ""
    while cociente_hexa > 0:
        resto_hexa = cociente_hexa % 16
        cociente_hexa = cociente_hexa // 16

        res_str = str(resto_hexa)
        res_st += res_str + " "

    for i in res_st:
        if i != " " and i != ".":  # procesa caracteres
            if ant != " ":
                ant_st = str(ant)
                i_st = str(i)
                num = ant_st + i_st
            elif ant == " ":
                i_st = str(i)
                num = i
        else:  # Procesar palabras

            if num == "15":
                num = "F"
            elif num == "14":
                num = "E"
            elif num == "13":
                num = "D"
            elif num == "12":
                num = "C"
            elif num == "11":
                num = "B"
            elif num == "10":
                num = "A"

            resultado = resultado + num
        ant = i

    if cociente_hexa == 1:
        resultado = resultado + str(cociente_hexa)

    stra = resultado
    res = len(stra)

    dado_vuelta = stra[res::-1]
    decimal = input("Ingrese el numero decimal: ")
    cant = int(input("Ingrese la cantidad de decimales que necesite:"))
    decimal = "0." + decimal
    decimal = float(decimal)

    part_deci = 0
    enteros = ""
    numero_1 = 0
    ant_1 = num_1 = ""
    resultado_1 = ""

    for a in range(cant):
        numero_1 = decimal * 16
        part_deci = numero_1
        numero_1 = int(numero_1)
        decimales = round(part_deci - numero_1, 2)
        tupla_num = str(numero_1)
        enteros = enteros + tupla_num + " "
        decimal = decimales

    for i in enteros:
        if i != " " and i != ".":  # procesa caracteres
            if ant_1 != " ":
                ant_st = str(ant_1)
                i_st = str(i)
                num_1 = ant_st + i_st
            elif ant_1 == " ":
                i_st = str(i)
                num_1 = i
        else:  # Procesar palabras

            if num_1 == "15":
                num_1 = "F"
            elif num_1 == "14":
                num_1 = "E"
            elif num_1 == "13":
                num_1 = "D"
            elif num_1 == "12":
                num_1 = "C"
            elif num_1 == "11":
                num_1 = "B"
            elif num_1 == "10":
                num_1 = "A"

            resultado_1 = resultado_1 + num_1
        ant_1 = i

    numero_convertido = dado_vuelta + "." + resultado_1
    return numero_convertido


def binario(cociente_hexa):

    ant = num = ""
    resultado = ""
    resto_hexa = cociente_hexa
    # HEXADECIMAL

    res_st = ""
    while cociente_hexa > 1:
        resto_hexa = cociente_hexa % 2
        cociente_hexa = cociente_hexa // 2

        res_str = str(resto_hexa)
        res_st += res_str + " "

    if cociente_hexa == 1:
        resultado = res_st + str(cociente_hexa)

    stra = resultado
    res = len(stra)

    dado_vuelta = stra[res::-1]
    decimal = input("Ingrese el numero decimal: ")
    cant = int(input("Ingrese la cantidad de decimales que necesite:"))
    decimal = "0." + decimal
    decimal = float(decimal)

    part_deci = 0
    enteros = ""
    numero_1 = 0
    ant_1 = num_1 = ""
    resultado_1 = ""

    for a in range(cant):
        numero_1 = decimal * 2
        part_deci = numero_1
        numero_1 = int(numero_1)
        decimales = round(part_deci - numero_1, 2)
        tupla_num = str(numero_1)
        enteros = enteros + tupla_num + " "
        decimal = decimales

    numero_convertido = dado_vuelta + "." + enteros

    return numero_convertido"""