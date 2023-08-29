cadena = input("Introdice una palabra o frase: ")
if len(cadena) == 0:
    print("No se introdujo ninguna palabra o frase para validar")
else:
    cadena_al_revez = cadena[::-1]
    if cadena.lower().replace(" ", "") == cadena_al_revez.lower().replace(" ", ""):
        print("La palabra o frase SI es un palindromo")
        print(
            f"""
            Palabra o frase original: {cadena}, 
            Palabra o frase al revez: {cadena_al_revez}
            """
        )
    else:
        print("la palabra o frase NO es un palindromo")
        print(
            f"""
            Palabra o frase original: {cadena}, 
            Palabra o frase al revez: {cadena_al_revez}
            """
        )
