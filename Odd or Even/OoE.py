numbers = [3, 4, 8, 2, 1]

odd = 0
even = 0

for i in numbers:
    if i % 2 == 0:
        even += i
    else:
        odd += i

print([even, odd])