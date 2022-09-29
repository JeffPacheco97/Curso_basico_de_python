
#FUNCIÓN PRINCIPAL
def run():
#ESTABLECEMOS LA RPTA DE LA ADIVINANZA
    respuesta = "Aguacate"
#DELIMITAMOS LA CANTIDAD DE INTENTOS POSIBLES
    intentos = 5
#PLANTEAMOS EL ENIGMA Y SOLICITAMOS UNA RESPUESTA
    adivinanza = input("Agua pasó por aquí, cate que no te vi. ¿La respuesta es?: ") 
#CONDICIONAL QUE INDICA SI LA ADIVINANZA DEL USUARIO EQUIVALE A LA RESPUESTA    
    if adivinanza == respuesta:
        print("¡Muy bien! Has ganao.")
#MIENTRAS LA ADIVINANZA DEL CLIENTE NO CORRESPONDA A LA RESPUESTA LE PEDIREMOS UNA RESPUESTA
    while adivinanza != respuesta:
#CADA FALLO EL USUARIO PIERDE UN INTENTO
        intentos -= 1 
#REPETIMOS EN CICLO HASTA QUE INDIQUE LA RPTA CORRECTA
        adivinanza = input("Lo lamento, no es la respuesta correcta. Intenta nuevamente, tienes " + str(intentos) + " intentos más: ")
#SI LO HACE LO FELICITAMOS
        if adivinanza == respuesta:
          print("¡Muy bien! Has ganao.")   
#SINO LE INDICAMOS QUE PERDIÓ
        if intentos == 0:
          print("Sorry, pero perdiste.")
          break
#AGRADECEMOS LA GRATA EXPERIENCIA
print("¡Gracias por jugar conmigo!")



#FUNCIÓN DE ENTRADA
if __name__ == '__main__':
    run()