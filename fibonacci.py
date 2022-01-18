# Escribe una función llamada fibonacci. Esta función recibe como parámetro un 
# número entero positivo. La función se encarga de imprimir la serie de fibonacci.
# El número recibido como parámetro es la cantidad de números a imprimir.
# Serie = 0 1 1 2 3 5 8 13 21 34 55 89

def fibonacci( num ):
    x1 = 0
    x2 = 1
    for n in range( 0, num ):
        if n % 2 == 0:
            print( x1 )
            x1 += x2
        else:
            print( x2 )
            x2 += x1

fibonacci( 30 )