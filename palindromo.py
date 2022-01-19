# Escribe una función llamada palindromo. Esta función recibe como parámetro
# un string. La función se encarga de retornar True si el string es un palindromo
# False de lo contrario.
# Palíndromos: radar - oso - arañera - orejero - rayar - salas - seres - sometemos
# BONUS: "Anita lava la tina" - "No traces en ese carton" - "Son robos o sobornos"

def palindromo( palabra ):
    inicio = 0
    final = len( palabra ) - 1

    while inicio < len( palabra ) / 2:
        if palabra[inicio] != palabra[final]:
            return False
        inicio += 1
        final -= 1
    return True


print( palindromo( "orejero" ) )