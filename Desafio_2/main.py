import

p = int(input("Ingrese un nuemero"))
print(p)
suma = p
cont = 1
lista = []
while p > 1:
    cont += 1
    if p % 2 == 0:
        p = p // 2
    else:
        p = 3 * p + 1
    suma += p

    lista.append(p)

print("Cantidad de valores", cont)
prom = suma / cont
print("Mayor", max(lista))
print("El promedio es:", round(prom,1))
