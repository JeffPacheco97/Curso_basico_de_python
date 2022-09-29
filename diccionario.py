#MÉTODO PRINCIPAL
def run():
    poblacion_paises = {
        'Argentina': 78894556,
        'Colombia': 45124578,
        'Brasil': 369852147,
    }


    menu = """
    
    Elige un país para saber el número de población que tiene.
    
    Presiona 1 para Argentina.
    Presiona 2 para Colombia.
    Presiona 3 para Brasil.

    Presiona 0 para salir.
    
    ¡Muy pronto más paises! 
    
    """    

    eleccion = 4
    while eleccion != 0:
        eleccion = int(input(menu))
        
        if eleccion == 1:
            print("La respuesta a tu país Argentina es: " + str(poblacion_paises['Argentina']))
            continue
        elif eleccion == 2:
            print("La respuesta a tu país Colombia es: " + str(poblacion_paises['Colombia']))
            continue
        elif eleccion == 3:
            print("La respuesta a tu país Brasil es: " + str(poblacion_paises['Brasil']))
            continue
        elif eleccion >=4:
            print("¿Por qué eres así? Ingresa un número válido.")

    
    print("¡Gracias por usar tu contador de población mundial de confianza!")



# #CICLO FOR QUE IMPRIME EL NOMBRE DE LAS LLAVES
# for pais in poblacion_paises.keys():
#         print(pais)
# #CICLO FOR QUE IMPRIME EL VALOR DE LAS LLAVES
# for pais in poblacion_paises.value():
#         print(pais)


#PUNTO DE ENTRADA
if __name__ == '__main__':
    run()