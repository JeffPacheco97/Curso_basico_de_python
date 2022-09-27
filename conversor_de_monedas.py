#SOLICITAR VALOR EN COP
pesos = input("¿Cuántos pesos colombianos tienes?: ")

#CASTEAR VALORES DE STR A FLOTANTE
pesos = float(pesos)

#SOLICITAR TASA DE CAMBIO
valor_dolar = input("¿A cuánto equivale el dolar hoy?")

#CASTEAR VALORES DE STR A FLOTANTE
valor_dolar = float(valor_dolar)

#REALIZAR CONVERSIÓN
conversion = pesos / valor_dolar

#REDONDEAR A DOS CON ROUND
conversion = round(conversion,2)

#CASTEAR VALORES DE STR A FLORTANTE
conversion = str(conversion)

#CASTEAR NUEVAMENTE PESOS DE FLOAT A STR PARA IMPRIMIR
pesos = str(pesos)

#IMPRIMIR RESULTADOS
print("El valor en dólares de sus $" + pesos + " es: $" + conversion)
