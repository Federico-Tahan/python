print("="*40)
print("      GENERADOR DE EMAIL")
print("="*40)

#ENTRADA
Nombre = input("Ingrese un Nombre: ") #se podria poner un .lower() EJ: Nombre = input("Ingrese un Nombre: ").lower()
Apellido = input("Ingrese un Apellido: ")
Dominio = input("Ingrese un Dominio: ")

#PROCEDIMIENTO

#upper PASAR STRING A MAYUSCULAS
#lower PASAR STRING A MINISCULAS

Nombre = Nombre.lower()
Apellido = Apellido.lower()
Dominio = Dominio.lower()


if Nombre [0] != Apellido [0]:
    Email = Nombre[0] + "." + Apellido + "@" + Dominio
else:
    Email = Nombre + "." + Apellido + "@" + Dominio


#Salida
print("Direccion de Email:", Email, sep="")# SEP AL FINAL SACA LOS ESPACIOS AL LAO DE LA ,,,

