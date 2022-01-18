# Escribe una función llamada numerosPrimos. Esta función recibe como parámetro
# un número entero positivo. La función se encarga de crear un arreglo con los
# números primos desde el 1 hasta el número proporcionado. La función retorna
# el arreglo como resultado.
# 30 => [ 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]

def esPrimo( num ):
    cont = 0
    for x in range( 1, num + 1 ):
        if num % x == 0:
            cont += 1
    if cont <= 2:
        return True
    else:
        return False

def numerosPrimos( rango ):
    primos = []
    for x in range( 1, rango + 1 ):
        if esPrimo( x ) == True:
            primos.append( x )
    return primos

resultado = numerosPrimos( 30 )
print( resultado )
