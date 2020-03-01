mnth = int( input( "input month number( 1-12): "))
lst_of_mnth = ("winter", "winter",
               "spring", "spring", "spring",
               "summer", "summer", "summer",
               "autumn", "autumn", "autumn",
               "winter")
print( lst_of_mnth[mnth-1])
dict_of_mnth = {"winter": (1, 2, 12),
                "spring": (3, 4, 5),
                "summer": (6, 7, 8),
                "autumn": (9, 10, 11)}
for tm_of_yr in dict_of_mnth.keys():
    if mnth in dict_of_mnth.get( tm_of_yr):
        print( tm_of_yr)
        break