num = int(input('Enter the number that you want to reverse : \n'))

reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num //= 10

print('Reversed Number is : ', reverse)