prcd = int( input( "input proceeds "))
outl = int( input( "input outlay "))
sld = prcd - outl

if sld > 0:
    print( "The firm has a profit.")
    prs_qty = int(input( "input personnel quantity "))
    rent = ( sld / prcd) / prs_qty
    print( f"The firm rentability is {rent}")
else:
    print( "The firm has a loss.")

