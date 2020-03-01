wrd_lst = input( "input words with spaces between them: ").split(" ")

for ind in range( len(wrd_lst)):
    print( f"{ind+1}: {wrd_lst[ind][:10]}")
