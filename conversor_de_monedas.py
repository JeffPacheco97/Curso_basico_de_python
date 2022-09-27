#FUNCIÓN DE CONVERTIR MONEDA
def convertir_moneda(tipo_moneda):
    #SOLICITAR VALOR de MONEDA
    moneda = input("¿Cuántos " + tipo_moneda + " tienes?: ")

#CASTEAR VALORES DE STR A FLOTANTE
    moneda = float(moneda)

#SOLICITAR TASA DE CAMBIO
    valor_dolar = input("¿A cuánto equivale el dolar hoy?")

#CASTEAR VALORES DE STR A FLOTANTE
    valor_dolar = float(valor_dolar)

#REALIZAR CONVERSIÓN
    dolares = moneda / valor_dolar

#REDONDEAR A DOS CON ROUND
    dolares = round(dolares,2)

#CASTEAR VALORES DE STR A FLORTANTE
    dolares = str(dolares)

#CASTEAR NUEVAMENTE PESOS DE FLOAT A STR PARA IMPRIMIR
    moneda = str(moneda)

#IMPRIMIR RESULTADOS
    print("El valor en dólares de sus $" + moneda + " es: $" + dolares + " dólares")


#INTERFAZ
#DESPLIEGUE DE MENU SOLICITANDO TIPO DE TASA DE CAMBIO
menu = """🪙 ¡Bienvenido a Convertland, tu convertidor de monedas favorito! 🪙

1-Pesos colombianos (COP)
2-Pesos Mexicanos (MXN)
3-Pesos Argentinos (ARS)

Elige la opción que más se adapte a tus necesidades. 😸
"""
opcion = int(input(menu))


#OPCIÓN 1 
if opcion == 1:
    convertir_moneda("pesos colombianos (COP)" )

#OPCIÓN 2 
elif opcion == 2:
    convertir_moneda("pesos mexicanos (MXN)")

#OPCIÓN 3 
elif opcion == 3:
    convertir_moneda("pesos argentinos (ARS)") 
      
#OPCIÓN DEFAULT
else:
    print("Ingresa un valor válido, no seas así. 😿")



