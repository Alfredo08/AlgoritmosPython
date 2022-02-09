# Escribe una función llamada palindromoRecursivo. Esta función recibe como parámetro
# un string. La función se encarga de retornar True si el string es un palindromo
# False de lo contrario.

def palindromoRecursivo( texto ):
    if len( texto ) <= 1:
        return True
    else:
        if texto[0] != texto[ len(texto) - 1 ]:
            return False
        else:
            return palindromoRecursivo( texto[1:-1] )

print( palindromoRecursivo( "radar" ) )