#SOLICITAMOS NUMERO A MULTIPLICAR
numero = int(input("¿De cuál número desea obtener la tabla de multiplicar?: "))
#INICIAMOS CICLO FOR EN RANGO DE 1 A 11 PARA TENER NUMEROS DE 0 A A 10
for i in range(1,11):
#MULTIPLICAMOS EL NUMERO DE USUARIO POR EL CONTADOR
    multiplicacion = numero * i
#IMPRIMIMOS EL RESULTADO EN UNA TABLA
    print("El número ingresado es: " + str(numero) + " y su tabla es: " + str(multiplicacion))