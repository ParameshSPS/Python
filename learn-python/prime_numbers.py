prime_numbers = []
for i in range(1, 21):
    if i > 1:
        for y in range(2, i):
            if (i % y) == 0:
                break
    else:
        prime_numbers.append(i)

print(prime_numbers)