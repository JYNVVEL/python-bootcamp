ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']


print(ranks[-4],ranks[-3],ranks[-2],ranks[-1],ranks[0])

ranks = *ranks[-4:],ranks[0]
print(f"{ranks}")