import sys

##CAPTURA DE DATOS##
nombre = input("ingresa tu(s) nombre(s): ")
if len(nombre) == 0:
    print("No ingresarte ningun dato como nombre.")
    sys.exit()

apellido_paterno = input("Ingresa apellido paterno: ")
if len(apellido_paterno) == 0:
    print("No ingresarte ningun dato como apellido paterno.")
    sys.exit()

apellido_materno = input("Ingresa apellido materno: ")
if len(apellido_materno) == 0:
    print("No ingresarte ningun dato como apellido materno.")
    sys.exit()

edad = input("Ingresa tu edad: ")
try:
    edad = float(edad)
    if edad <= 0:
        print("La edad no puede ser '0' o menor.")
except ValueError:
    print("Los datos ingresados no son correctos.")

peso = input("Ingresa tu peso en KG:")
try:
    peso = float(peso)
    if peso <= 0:
        print("El peso no puede ser '0' o menor.")
        sys.exit()
except ValueError:
    print("Los datos ingresados no son correctos.")
    sys.exit()

estatura = input("Ingresa tu estatura en CM:")
try:
    estatura = float(estatura)
    if estatura <= 0:
        print("La estatura no puede ser '0' o menor.")
        sys.exit()
    estatura = estatura / 100
    print("\b")
except ValueError:
    print("Los datos ingresados no son correctos.")
    sys.exit()

imc = peso / (estatura**2)
print(
    f"""
        Nombre: {nombre}
        Apellidos: {apellido_paterno} {apellido_materno}
        Edad: {int(edad)} Años.
        Peso: {peso} Kg.
        Estatura: {estatura} Mts.
        IMC: {imc:.2f}"""
)
sys.exit()
