"""may_carta = None
may_palo = 0
palo_1 = input("Ingrese el palo de la primera carta: ")
carta_1 = int(input("Ingrese el numero de la carta: "))
palo_2 = input("Ingrese el palo de la segunda carta: ")
carta_2 = int(input("Ingrese el numero de la segunda carta:"))
palo_3 = input("Ingrese el palo de la tercera carta: ")
carta_3 = int(input("Ingrese el numero de la tercera carta: "))

if carta_1 > carta_2 and carta_1 > carta_3:
    may_carta = carta_1
    may_palo = palo_1
elif carta_2 > carta_3:
    may_carta = carta_2
    may_palo = palo_2
else:
    may_carta = carta_3
    may_palo = palo_3

suma = carta_1 + carta_2 + carta_3

print()
print("*"* 50)
print("La carta mayor fue el", may_carta, "de", may_palo)
print("La suma de las cartas fue", suma)
if palo_1 != palo_2 and palo_1 != palo_3 and palo_2 != palo_3:
    print("Las cartas son de distinto palo")
print("*" * 50)"""
__author__ = "Federico Tahan 89351"

opcion = None

while opcion != 3:
    print("=" * 30)
    print("\tMenú de opciones")
    print("=" * 30)
    print()
    print("1-Procesamiento de cartas")
    print("2-Procesamiento de multiplos")
    print("3-Salir del programa")
    print()

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        cartas = 3
        mey_pal = None
        mey_num = 0
        suma = 0
        palo_1 = None
        palo_2 = None
        palo_3 = None
        for i in range(cartas):
            palo = input("Ingrese el palo de la carta: ")
            numero = int(input("Ingrese el número de la carta: "))

            if i == 0 or mey_num < numero:
                mey_pal = palo
                mey_num = numero

            suma += numero

            if i == 0:
                palo_1 = palo
            elif i == 1:
                palo_2 = palo
            elif i == 2:
                palo_3 = palo
        print()
        print("*" * 50)
        print("La carta mayor fue", mey_num, "de", mey_pal)
        print("La suma de los naipes fue", suma)
        if palo_1 != palo_2 and palo_1 != palo_3 and palo_2 != palo_3:
            print("Las cartas son de distinto palo")
        print("*" * 50)
        print()
    elif opcion == 2:
        prom = 0
        multiplo = 0
        vueltas = 0
        prom_gral = 100
        numero = int(input("Ingrese un numero entre el 1 y 9: "))

        while numero < 1 or numero > 9:
            print("El número ingresado no es correcto")
            numero = int(input("Ingrese un numero entre el 1 y 9: "))

        sec = int(input("Ingrese una secuencia de números(la carga finaliza cuando ingrese 0): "))
        while sec != 0:
            vueltas += 1
            if sec % numero == 0:
                multiplo += 1
            sec = int(input("Ingrese una secuencia de números(la carga finaliza cuando ingrese 0): "))
        prom_multi = multiplo * 100 / vueltas

        prom_no_multi = prom_gral - prom_multi
        print()
        print("*" * 50)
        print("El promedio de los multiplos en el total de la serie ingresada fue del", round(prom_multi), "%")
        if prom_multi > prom_no_multi:
            print("El promedio de los multiplos es mayor al promedio general")
        elif prom_multi < prom_no_multi:
            print("El promedio de los multiplos es menor al promedio general")

        print("*" * 50)
        print()
    elif opcion != 3:
        print("Programa Finalizado")
    else:
        print("La opcion no es valida")
