
def reverseRecursivo( texto ):
    if len( texto ) == 1:
        return texto
    else:
        ultimoIndice = len( texto ) - 1
        return texto[ultimoIndice] + reverseRecursivo( texto[:-1] )

print( reverseRecursivo( "Hola, me gusta mucho programar!" ) )