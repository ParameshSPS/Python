list1 = []

[list1.append(i) for i in range(1, 51)]

print(list1[::-1])

print(list1[::2])

print(list1[0:20:2])

fruits = ['mango', 'pomogranate', 'guava']

fruits.reverse()

# rev = list(fruits)

rev = fruits.copy()

print(rev)