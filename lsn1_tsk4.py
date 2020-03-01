p_i_n = int( input( "input positive integer "))
max = int(0)
while( p_i_n):
    l_s = p_i_n % 10
    if max < l_s:
        max = l_s
    p_i_n //= 10
print( max)