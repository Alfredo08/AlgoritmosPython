# 5! = 1 * 2 * 3 * 4 * 5 
# 5 = 1 + 2 + 3 + 4 + 5

def factorialRecursivo( num ):
    if num == 1:
        return 1
    else:
        return num * factorialRecursivo( num - 1 )

print( factorialRecursivo( 6 ) )