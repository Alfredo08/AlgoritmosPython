# Crear la función bubbleSort. Esta función recibe un arreglo que contiene números enteros.
# La función se encarga de ordenar de menor a mayor el contenido del arreglo y lo retorna.
# [4, 9, 6, 1, 8, 2, 7, 5, 3, 10] => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def bubbleSort( numeros ):
    for i in range( 0, len( numeros ) - 1 ):
        for j in range( i + 1, len( numeros ) ):
            if numeros[i] > numeros[j]:
                aux = numeros[i] 
                numeros[i] = numeros[j]
                numeros[j] = aux
    return numeros

arr = [4, 9, 6, 1, 8, 2, 7, 5, 3, 10]

print( bubbleSort( arr ) )