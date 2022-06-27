# A positive integer is called an Armstrong number of order n if

# abcd... = an + bn + cn + dn + ...

# In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.


num  = int(input("Enter a Number: "))

sum = 0

temp = num

while temp > 0:
    digit = temp % 10
    sum += (digit ** 3)
    temp //= 10

if num == sum:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")

