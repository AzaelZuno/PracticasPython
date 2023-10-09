# Validar longitud de una palabra


#Longitud palabra Solucion 1
#Se define una funcion para validar la longitud de una palabra
""" def Validar_longitud(palabra):
    #se inicializa el contador para guardar el numero de letras que contiene la palabra 
    contar_letras = 0
    #Se utiliza el For para iterar en cada letra de la palabra y se suma en 1 cada iteracion en el contador.
    for letras in palabra:
        contar_letras += 1
    # Se valida que la longitud de la palabra no sea menor a 4 letras, indicando con un mensaje la cantidad de letras que contiene la palabra.
    if contar_letras < 4:
        mensaje = print(f"Hacen falta letras. La palabra {palabra} solo contiene {contar_letras} letras")
        return mensaje
    #Se valida que la longitud de la palabra no sea mayor a 8 letras, indicando con un mensaje la cantidad de letras que contiene la palabra.
    if contar_letras > 8:
        mensaje = print(f"Sobran letras. La palabra {palabra} tiene {contar_letras} letras")
        return mensaje
    #Si la palabra cumple con la longuitud correcta, se indica mediante un mensaje
    else:

        mensaje = print(f"la palabra {palabra} tiene la longitud correcta")
        return mensaje

#Se ingresa la palabra mediante teclado.
palabra = input("Ingresa una palabra de 4 a 8 caracteres: ")
#Se manda a llamar la funcion para validar la longuitud de la palabra
Validar_longitud(palabra) """

# Longitud palabra Solucion 2
"""def Validar_Longitud2(palabra2):
    #Se inicializa la variable palabra utilizando la funcion len() para obtener la longuitud de la palabra
    longitud = len(palabra2)

    if longitud < 4:
        mensaje = print(f"Hacen falta letras. La palabra {palabra2} solo contiene {longitud} letras")
        return mensaje

    if longitud > 8:
        mensaje = print(f"Sobran letras. La palabra {palabra2} tiene {longitud} letras")
        return mensaje
    else:
        mensaje = print(f"la palabra {palabra2} tiene la longitud correcta")
        return mensaje


palabra2 = input("Ingresa una Palabra de 4 a 8 caracteres: ")
Validar_Longitud2(palabra2)"""


#Cordenadas Solucion1
try:
    x=int(input("Ingresa las cordenada en eje 'X':"))
    y=int(input("Ingresa las cordenada en eje 'Y':"))
    #Se inicializa una lista llamada "Cordenadas", se inicializan los valores de los elementos con las variables X e Y
    cordenadas =[x,y]
    #Se valida los valores de los elementos de la lista para determinar en que cuadrante se encuentran
    if cordenadas == [0,0]:
        print("Las cordenadas se encuentran en el ORIGEN")
    elif cordenadas[0] > 0 and cordenadas[1] > 0:
        print("Las cordenadas se encuentran en el CUADRANTE 1")
    elif cordenadas[0] < 0 and cordenadas[1] > 0:
        print("Las cordenadas se encuentran en el CUADRANTE 2")
    elif cordenadas[0] < 0 and cordenadas[1] < 0:
        print("Las cordenadas se encuentran en el CUADRANTE 3")
    elif cordenadas[0] > 0 and cordenadas[1] < 0:
        print("Las cordenadas se encuentran en el CUADRANTE 4")
    elif cordenadas[0] == 0 :
        print("Las cordenadas se encuentran sobre el eje 'Y'")
    elif cordenadas[1] == 0 :
        print("Las cordenadas se encuentran sobre el eje 'X'")
except ValueError:
    print("Datos ingresados INCORRECTOS")






















