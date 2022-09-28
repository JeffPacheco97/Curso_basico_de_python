def run():

    
# #SOLICITAMOS NOMBRE AL USUARIO
#     nombre = input("Escribe tu nombre: ")
# #GUARDAMOS EN LA VARIABLE LETRA LO RECORRIDO EN LA VARIABLE NOMBRE POR CICLO
#     for letra in nombre:
#         print(letra)


# #SOLICITAMOS NOMBRE AL USUARIO
    frase = input('Escribe tu frase favorita: ')
#GUARDAMOS EN LA VARIABLE CHAR LO RECORRIDO EN LA VARIABLE FRASE POR CICLO

    for char in frase:
        print(char.replace(" ", "*").upper())





if __name__ == '__main__':
    run()