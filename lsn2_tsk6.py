gds_lst = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

gds_anl = {}
for good_key in gds_lst[0][1].keys():
    tmp_arr = []
    for good in gds_lst:
        tmp_arr.append(good[1].get(good_key))
    gds_anl.setdefault(good_key, list( set(tmp_arr)))

print( gds_anl)
