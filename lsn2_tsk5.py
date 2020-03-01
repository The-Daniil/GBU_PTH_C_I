rate_lst = [7, 5, 3, 3, 2]

nw_elem = int( input( "input new element of rate: "))

for ind in range( len( rate_lst)):
    if nw_elem > rate_lst[ind]:
        rate_lst.insert( ind, nw_elem)
        break
if ind+1 == len( rate_lst): rate_lst.append( nw_elem)
print( rate_lst)