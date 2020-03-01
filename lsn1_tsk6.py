a = float( input( "input first day result "))
b = float( input( "input result "))

d_nmb = 1;
while a < b:
    a += a / 10
    d_nmb += 1
print( d_nmb)