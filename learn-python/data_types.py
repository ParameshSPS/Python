# Python has the following data types built-in by default, in these categories:
# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview

x = -5

y = 34.5

z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))
print(z)


# Radom Number

import random

print(random.randrange(1,10))


a = 'Hari Krishna'

print(a[0:6])

print(a[-5:-1])


y = ''
for x in reversed(a):
    print(y + x)


string = 'My name is {0}. I am from {2}, which is located in {1}'

print(string.format('Hari Krishna', 'Anantapur', 'Dharmavaram'))