def get_line():
    """ Считывает разделённые пробелом слова в список"""
    return list( input().split(" "))


def increase_sum( lst):
    """ Увеличивает общую сумму на значения из списка

    lst -- список чисел в иде строк
    """
    s=0
    for num in lst:
        s += int( num)
    return s


FLAG_END = False
all_sum = 0
print( "input numbers divided by ' ':")
while True:
    line = get_line()
    if line.count( "^Q") > 0:
        line = line[:line.index( "^Q")]
        FLAG_END = True
    all_sum += increase_sum( line)
    print( all_sum)
    if FLAG_END: break

