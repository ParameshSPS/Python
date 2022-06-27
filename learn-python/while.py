a = 1

while a <= 6:
    print(a)
    a += 1
else:
    print('A is no longer less than 6')

a = 0

while a <= 6:

    a += 1
    if (a == 3):
        break
    print(a)
else:
    print('A is no longer less than 6')

a = 0
while a < 6:

    a += 1
    if (a == 3):
        continue
    print(a)
