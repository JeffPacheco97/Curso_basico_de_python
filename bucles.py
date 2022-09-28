
#FUNCIÓN PRINCIPAL
def run():
    #CREAMOS UN LÍMITE PARA EL BUCLE
    LIMITE = 10
    #CREAMOS UN CONTADOR
    contador = 0
    #SOLICITAMOS UN NUMERO ENTERO
    numero = int(input("Ingresa un número entero: "))
    #POTENCIA
    potencia_2 = numero**contador

    while contador < LIMITE:
    #IMPRIME EL RESULTADO
        resultado = print("La potencia de tu número "+ str(numero) + " elevado a "+ str(contador) +" equivale a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = numero**contador


#FUNCIÓN DE ENTRADA
if __name__ == '__main__':
    run()

