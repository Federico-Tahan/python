#print("=" * 42)
#print("Conversiones de unidades de Tiempo Segundo a Hora")
#print("=" * 42)

#Entradas

Tiempo = int(input("Ingrese el tiempo en segundos: "))


#Procedimiento

Horas = Tiempo // 3600
Minutos = (Tiempo // 60) % 60
Segundos = Tiempo % 60

#Salida
print("El tiempo trasncurrido fue de", Horas, "horas,", Minutos, "Minutos,", Segundos, "Segundos")



#Primera Ejecucion: 1:49:11 = 6551segs
#Segunda Ejecucion: 6:2:0 = 21720 segs
#Tercera Ejecucion: 0:52:3 = 3123 segs
#Cuarta Ejecucion: 16:4:22 = 57862


#=================================================================================================================
#=====================================PROCESO AL REVES============================================================
#=================================================================================================================

#print("=" * 42)
#print("Conversiones de unidades de Tiempo Hora a Segundo")
#print("=" * 42)

#Entradas
#Tiempo = input("Ingrese el tiempo con formato horas:minutos:segundos: ")


#Hora = Tiempo[0:2]
#Hora_int = int(Hora)

#Minutos= Tiempo[3:5]
#Minutos_int = int(Minutos)

#Segundos = Tiempo[6:8]
#Segundos_int = int(Segundos)

#Procedimiento
#Hora_s = Hora_int * 3600
#Minutos_s = Minutos_int * 60
#Total_seg = Hora_s + Minutos_s + Segundos_int

#Salidas
#print(Tiempo,"Tiene una cantidad de ", Total_seg, "Segundos")

#a= input("ingresa el nombre de un filosofo: ")
#Socrates
#01234567
#Indice = a[3:5]
#VA DEL 3 AL 4 SIN TOCAR EL 5
#print(Indice)
