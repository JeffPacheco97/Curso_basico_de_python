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
print("Sus $"+ mxn + " pesos mexicanos (MXN) equivalen a: $" + dolar)


