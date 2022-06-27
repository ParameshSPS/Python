elelist = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 9, 7, 11, 34, 66, 44, 7]

newdict = {}

for ele in elelist:
    if ele in newdict:
        newdict[ele] += 1
    else:
        newdict[ele] = 1

print(newdict)