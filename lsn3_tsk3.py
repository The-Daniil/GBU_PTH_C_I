def my_func( *args):
    """Возвращает сумму двух наибольших параметров"""
    lst = list(args)
    lst.sort()
    return sum( lst[-2:])


print( my_func( 2, 3, 8))
