

file = open('test.txt', 'a')

# print(file.read())

# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)

file.write("\nNew Line added from the code")

file.close()

file = open('test.txt', 'r')

for line in file:
    print(line)

file.close()