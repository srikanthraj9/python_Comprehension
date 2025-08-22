# Without dictionary  comprehension

numbers = [1, 2, 3, 4, 5]
squares_dict = {}
for n in numbers:
    squares_dict[n] = n**2
print(squares_dict)

# With dictionary comprehension

numbers = [1, 2, 3, 4, 5]
squares_dict = {n: n**2 for n in numbers}
print(squares_dict)

