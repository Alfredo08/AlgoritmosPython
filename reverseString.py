# Escribe una función llamada reverseString. Esta función recibe como parámetro
# un string. La función se encarga de retornar el string recibido pero en orden
# de atrás hacia adelante.
# "Hola como estas" => "satse omoc aloH"

def reverseString( texto ):
    resultado = ""
    for i in range( len( texto ) -1, -1, -1 ):
        resultado += texto[i]
    return resultado

texto = "Hola como estas"

print( reverseString( texto) )


