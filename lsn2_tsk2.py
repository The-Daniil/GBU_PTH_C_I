lst1 = input( "input elements with spaces between them: ").split(" ")

for i in range(1, len(lst1), 2):
    lst1[i], lst1[i-1] = lst1[i-1], lst1[i]
print( lst1)