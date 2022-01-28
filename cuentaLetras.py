
# Escribe una función llamada cuentaLetras. Esta fucnión recibe como parámetro
# un string. La función debe de retornar un diccionario con el número de veces
# que se encuentra cada letra dentro del string.
oracion = "Hola como estas" 

def cuentaLetras( texto ):
    diccionario = {}
    for letra in texto:
        if letra in diccionario:
            diccionario[ letra ] += 1
        else:
            diccionario[ letra ] = 1
    return diccionario

print( cuentaLetras(oracion) )

