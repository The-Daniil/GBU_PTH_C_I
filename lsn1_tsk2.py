HOUR = 3600
MINUTE = 60

tm_sc_all = int( input("input sec: "))
tm_h = tm_sc_all // HOUR
tm_m = ( tm_sc_all % HOUR) // MINUTE
tm_sc = ( tm_sc_all % HOUR) % MINUTE
print( f"{tm_h}:{tm_m}:{tm_sc}")