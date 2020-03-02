def int_func( word):
    if str(word.islower()):
        return str(word).capitalize()
    else:
        return None


lst1 = input("input words separated by ' ': ").split(" ")
str1 = ' '.join(map( int_func, lst1))
print( str1)