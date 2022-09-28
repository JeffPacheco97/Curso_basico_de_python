#MÉTODO QUE DEFINE LOS PALÍNDROMOS
def palindromo(palabra):
#REEMPLAZA LOS ESPACIOS, LA PUNTUACIÓN Y LOS ACENTOS ELIMINÁNDOLOS
    palabra = palabra.replace(" ", "")\
        .replace("á", "a") \
        .replace("é", "e") \
        .replace("í", "i") \
        .replace("ó", "o") \
        .replace("ú", "u") \
        .replace(",", "") \
        .replace(".", "")
#CONVIERTE PALABRA A MINÚSCULA
    palabra = palabra.lower()
#INVIERTE LA PALABRA
    palabra_invertida = palabra[::-1]
#CONDICIONAL RETORNA TRUE SI SON IGUALES
    if palabra == palabra_invertida:
        return True
    else:
        return False

#FUNCIÓN PRINCIPAL
def run():
    palabra = input("Ingresa una palabra: ")

#EJECUTA FUNCIÓN PALÍNDROMO Y LA GUARDA EN LA VARIABLE ES_PALINDROMO
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print( palabra + " Es un palíndromo")
    else:
        print( palabra + " No es un palíndromo")

#PUNTO DE ENTRADA
if __name__ == '__main__':
    run()