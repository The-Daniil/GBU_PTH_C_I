def my_func( n, p=0):
    """Возводит число в степень

    n -- число
    p -- степень( default = 0)
    """

    if p == 0:
        return 1
    elif p < 0:
        return 1 / ( n * my_func( n, abs(p)-1))
    else:
        return n * my_func(n, p - 1)


n, p = input( "input number power: ").split(" ")
print( f"{n}^{p} = {my_func(float(n), int(p))}")