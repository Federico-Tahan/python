from funciones import *


def test():
    opcion = None
    v = []
    genero_num = None
    while opcion != 8:
        print("📕📗" * 60)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t 📕📗 Gestión de Libros 📗📕")
        print("📕📗" * 60)
        print()
        print("1. Generacion y carga")
        print("2. Mostrar")
        print("3. Conteo y género más popular: ")
        print("4. Filtrar el precio mayor por idioma: ")
        print("5. Búsqueda por ISBN: ")
        print("6. Consulta de un género: ")
        print("7. Consulta de precio por grupo: ")
        print("8. Finalizar programa: ")
        print()

        opcion = int(input("► Ingrese su opción: "))

        if opcion == 1:
            sub_menu = None
            while sub_menu != 3:
                print("► Ingrese el tipo de carga que desea realizar!")
                print("1. Carga Manual")
                print("2. Carga automatica")
                print("3. Volver")

                sub_menu = int(input("► Ingrese su opcion: "))

                if sub_menu == 1:
                    n = int(input("► Ingrese la cantidad de libros que desee registrar: "))
                    v = register(v, n)
                    register(v)
                    sub_menu = 3
                elif sub_menu == 2:
                    n = int(input("► Ingrese la cantidad de libros a registar: "))
                    v = []
                    v = register_auto(v, n)
                    sub_menu = 3
                elif sub_menu == 3:
                    pass
                else:
                    print("❌ Opcion no valida!")
        elif opcion == 2:
            if not v:
                print("❌ No se han proporcionado datos!")
            else:
                ordenar_libros(v)
                mostrar_vector(v)
        elif opcion == 3:
            if v:
                vc = libros_por_genero(v)
                mostrar_libros_genero(vc)
                b = gen_popular(vc)
                genero_num = b[0]
                genero_txt = conv_gen(genero_num)
                unidades = b[1]
                print("\n ✔ El genero con mayor cantidad de libros ofrecidos fue", genero_txt, "con", unidades, "unidades")
                print()
            else:
                print("❌ No se proporcionaron datos!")
        elif opcion == 4:
            print("► Ingrese el idioma que desee filtrar el precio.")
            idioma = int(input("► Ingrese el Idioma (1:español,2:Inglés,3:francés,4:italiano,5:otros): "))
            vector_agr_idm = agrupar_idioma(v, idioma)
            if vector_agr_idm:
                v_ord_price = ordenar_precios(vector_agr_idm)
                price_may = v_ord_price[0]
                print(to_string_titulo())
                print(mostrar_libro(price_may))
            else:
                print("❌ No se encontraron libros con ese idioma!")
        elif opcion == 5:
            identificador = input("► Ingrese el ISBN para buscar el libro: ")
            vector = search_isbn(v, identificador)
            if vector is not None:
                a = v[vector].pre * 10 / 100
                v[vector].pre += a
                print(to_string_titulo())
                print(mostrar_libro(v[vector]))
            else:
                print("❌ No existe ese identificador!")
        elif opcion == 6:
            if genero_num is not None:
                vector_gen_pop = agrupar_genero(v, genero_num)
                v_gen_price_order = ordenar_precios(vector_gen_pop)
                mostrar_vector(v_gen_price_order)
            else:
                print("❌ No se proporcionaron datos!")
        elif opcion == 7:
            identificacion = input("► Ingrese el codigo de idenficiacion (finaliza con 0):")
            v_libros_solicitados = libros_solicitados(identificacion, v)
            mostrar_vector(v_libros_solicitados)
            print("\n ✔ Precio total de los libros solicitados $", suma_precios(v_libros_solicitados))
        elif opcion == 8:
            print("✔ Programa finalizado.")
        else:
            print("❌ Opcion no valida!")


if __name__ == "__main__":
    test()
