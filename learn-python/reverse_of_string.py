
# one way

string = input('Enter a strig to reverse it : ')

reversed_string = ''

for x in range(len(string) - 1, -1, -1):
    
    reversed_string += string[x]

print(reversed_string)


# second way

# string = input('Enter a strig to reverse it : ')

# reversed_string = ''

# for x in string:
#     reversed_string = x + reversed_string

# print(reversed_string)

# third way

# string = 'Hari Krishna'

# reversed_string = string[::-1]

# print(reversed_string)

# fourth way

# reversed_string = ''.join(reversed(string));

# print(reversed_string)