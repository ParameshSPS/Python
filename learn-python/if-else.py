a, b, c = 223, 144, 55

if a > b and a > c:
    print('greatest number is', a)
elif b > a and b > c:
    print('greatest number is', b)
else:
    print('greatest number is', c)

a = 2
b = 330
print("A") if a > b else print("B") 

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 

N = int(input('Enter any Number: '))

if ((N%2 != 0) or (N<=6 and N>=20)):
    print('Weird')
else:
    print('Not Weird')
