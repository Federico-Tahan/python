"""__author__ = "Federico Yamil Tahan 89351"

opcion = None

while opcion != 4:
    print("=" * 30)
    print("\tMenú de opciones")
    print("=" * 30)
    print()
    print("1-Procesamiento de temperaturas")
    print("2-Procesamiento de carrera")
    print("3-Mostrar Resultados")
    print("4-Salir del programa")
    print()

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:

        localidades = 3
        menor_temp = 0
        menor_local = None
        for i in range(localidades):
            localidad = input("Ingrese aquí el nombre de la localidad: ")
            temp = int(input("Ingrese aquí la temperatura: "))

            if i == 0 or menor_temp > temp:
                menor_local = localidad
                menor_temp = temp
        print()
        temp_record = int(input("Ingrese la termperatura record: "))
        print()
        print("*" * 50)
        print("La localidad con menor temperatura fue", menor_local, "con", menor_temp, "°C")
        if menor_temp < temp_record:
            print("Frio record en la localidad de", menor_local)
        print("*" * 50)
        print()
    elif opcion == 2:
        timetot = 0
        time_men = 0
        time_may = 0
        name_men = None
        name_may = None

        corredores = int(input("Ingrese aquí la cantidad de corredores: "))

        for corr in range(corredores):
            name = input("Ingrese aquí el nombre del corredor: ")
            time = int(input("Ingrese aqui el tiempo (en segundos) del corredor: "))

            timetot += time

            if corr == 0 or time_men > time:
                time_men = time
                name_men = name

            if corr == 0 or time_may < time:
                time_may = time
                name_may = name

        promgral = timetot / corredores

        time_record = float(input("Ingrese aquí el tiempo record: "))

        print()
        print("*" * 50)
        print("El ganador fue", name_men, "con", time_men, "segundos")
        if time_men < time_record:
            print("Tiempo sobresaliente")
        print("Tiempo promedio de todos los corredores :", promgral, "segundos")
        print("*" * 50)
        print()
    elif opcion == 3:
        suma = 0

        numero = input("Ingrese aqui una serie de numeros: ")

        for a in numero:
            a = int(a)
            if a % 2 == 0:
                suma += a

        print("*" * 50)
        print("La suma comprendida en la secuencia es", suma)
        print("*" * 50)
        print()
    elif opcion == 4:
        print("Programa Finalizado")
    else:
        print("Opcion no valida")
"""

ant = None
end_voc = 0
cont = 0
txt = input("Ingrese el texto: ")
if txt[-1] != ".":
    txt = txt + "."
for let in txt:
    if let == " " and ant in "aeiouAEIOUáéíóúÁÉÍÓÚ" or let in ".,;:'" and ant in "aeiouAEIOUáéíóúÁÉÍÓÚ":
        end_voc += 1
    ant = let
print()
print(end_voc)