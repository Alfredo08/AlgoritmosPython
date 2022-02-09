# Escribe una función llamada fibonacciRecursivo. Esta función recibe como parámetro un 
# número entero positivo. La función se encarga de imprimir el número recibido de la serie de fibonacci.
# Ejemplo 10 => 34
# Serie = 0 1 1 2 3 5 8 13 21 34 55 89

def fibonacciRecursivo( num ):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacciRecursivo( num - 1 ) + fibonacciRecursivo( num - 2 )

print( fibonacciRecursivo( 5 ) )