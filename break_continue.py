#FUNCIÓN PRINCIPAL
def continue_1():
#INICIA UN CICLO CON RANGO DE 0 A 999
    for i in range(1000):
#PERO AL ENCONTRAR IMPARES NO LOS IMPRIME
        if i % 2 != 0:
#CONTINUE HACE QUE NO IMPRIMAMOS LO QUE SIGUE EN EL BLOQUE
            continue    
#FUNCIÓN IMPRIMIR 
        print(i)  


#FUNCION BREAK_1
def break_1():
#INICIA UN CICLO CON RANGO DE 0 A 9999
    for i in range(10000):
       print(i)
       if i == 5689:
#BREAK CORTA EL CICLO
        break            


#FUNCIÓN BREAK_2
def break_2():
#RECORRER UN STRING Y CORTAR EN UN PUNTO ESPECÍFICO
    animal = input("Ingresa tu animal favorito: ")
    for letra in animal:
        if letra == "a":
            break
        print(letra)



#FUNCIÓN DE INICIO
if __name__ == '__main__':
   #continue_1()
   #break_1()
    break_2()

