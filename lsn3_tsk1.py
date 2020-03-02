def division( dvs, dvd = 1.0):
    """Возвращает частное от деления

    Именованные параметры:
    dvs -- делимое
    dvd -- делитель( defoult = 1.0)

    """
    if type( dvs) == float \
            and type( dvd) == float \
            and dvd != 0:
        return float(dvs) / float(dvd)
    else:
        return None

n1, n2 = input( "input division and divider: ").split(" ")
print( f"division result: {division(n1, n2)}")