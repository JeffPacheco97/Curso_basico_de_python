
#DESPLIEGUE DE MENU SOLICITANDO TIPO DE TASA DE CAMBIO
menu = """🪙 ¡Bienvenido a Convertland, tu convertidor de monedas favorito! 🪙

1-Pesos colombianos (COP)
2-Pesos Mexicanos (MEX)
3-Pesos Argentinos (ARS)

Elige la opción que más se adapte a tus necesidades. 😸
"""
opcion = int(input(menu))

#OPCIONES A ELEGIR EN CONDICIONALES IF
if opcion == 1:

#SOLICITAR VALOR EN COP
    pesos = input("¿Cuántos pesos colombianos tienes?: ")

#CASTEAR VALORES DE STR A FLOTANTE
    pesos = float(pesos)

#SOLICITAR TASA DE CAMBIO
    valor_dolar = input("¿A cuánto equivale el dolar hoy?")

#CASTEAR VALORES DE STR A FLOTANTE
    valor_dolar = float(valor_dolar)

#REALIZAR CONVERSIÓN
    dolares = pesos / valor_dolar

#REDONDEAR A DOS CON ROUND
    dolares = round(dolares,2)

#CASTEAR VALORES DE STR A FLORTANTE
    dolares = str(dolares)

#CASTEAR NUEVAMENTE PESOS DE FLOAT A STR PARA IMPRIMIR
    pesos = str(pesos)

#IMPRIMIR RESULTADOS
    print("El valor en dólares de sus $" + pesos + " es: $" + dolares + " dólares")

    
elif opcion == 2:
#SOLICITAR CANTIDAD DE PESOS MEXICANOS DISPONIBLES
    mxn = input("¿Cuántos pesos mexicanos tienes?:  ")

#CASTEAR DE STR A FLOAT
    mxn = float(mxn)

#SOLICITAR TASA DE CAMBIO
    valor_dolar = input("¿Cuál es la tasa de cambio para el MXN hoy?")

#CASTEAR DE STR A FLOAT
    valor_dolar = float(valor_dolar)

#HACER CONVERSIÓN SEGÚN TASA DE CAMBIO
    dolar = mxn / valor_dolar

#REDONDEAR A DOS CON ROUND
    dolar = round(dolar, 2)

#CASTEAR DE FLOAT A STR
    dolar = str(dolar)

#CASTEAR NUEVAMENTE MXN DE FLOAT A STR
    mxn = str(mxn)

#IMPRIMIR VALORES EN PANTALLA
    print("Sus $"+ mxn + " pesos mexicanos (MXN) equivalen a: $" + dolar + " dólares")


elif opcion == 3:

#SOLICITAR CANTIDAD DE PESOS ARGENTINOS DISPONIBLES
    ars = input("¿Cuántos pesos argentinos tienes?:  ")

#CASTEAR DE STR A FLOAT
    ars = float(ars)

#SOLICITAR TASA DE CAMBIO
    valor_dolar = input("¿Cuál es la tasa de cambio para el ARS hoy?")

#CASTEAR DE STR A FLOAT
    valor_dolar = float(valor_dolar)

#HACER CONVERSIÓN SEGÚN TASA DE CAMBIO
    dolar = ars / valor_dolar

#REDONDEAR A DOS CON ROUND
    dolar = round(dolar, 2)

#CASTEAR DE FLOAT A STR
    dolar = str(dolar)

#CASTEAR NUEVAMENTE MXN DE FLOAT A STR
    ars = str(ars)

#IMPRIMIR VALORES EN PANTALLA
    print("Sus $"+ ars + " pesos argentinos (ARS) equivalen a: $" + dolar + " dólares")
    
else:
    print("Ingresa un valor válido, no seas así. 😿")



