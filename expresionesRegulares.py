import re

EXP_NOMBRE = re.compile( r'^[A-Z][a-zA-Z]+$' )

#if not EXP_NOMBRE.match( "alfredo" ):
#    flash( "El nombre unicamente debe contener letras" )
#else:
#    print( "Cumple con el patrón" )

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

if not EMAIL_REGEX.match( "avelez@codingdojo.com" ):
    print( "Hay algo que no cumple con el patrón" )
else:
    print( "Cumple con el patrón" )


EXP_PASSWORD = re.compile( r'^[a-zA-Z]{8,16}$')

if not EXP_PASSWORD.match( "alfredosalfredos" ):
    print( "Hay algo que no cumple con el patrón" )
else:
    print( "Cumple con el patrón" )