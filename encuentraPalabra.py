
# Escribe la función encuentraPalabra. Esta función recibe como parámetros:
# un arreglo de strings y un string. La función debe de retornar el número de 
# veces que se encuentra la palabra dentro del arrelgo de strings.

def encuentraPalabra( oracion, palabra ):
    cont = 0
    for pal in oracion:
        if pal == palabra:
            cont += 1
    return cont

texto = ["Hola", "como", "estas?", "Me", "gusta", "programar.", "También", "me", "gusta", "la", "música."]
palabra = "me"

print( encuentraPalabra( texto, palabra ) )