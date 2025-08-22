

# Without comprehension:

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = set()
for n in numbers:
    unique_squares.add(n**2)

print(unique_squares)


# With set comprehension:

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {n**2 for n in numbers}
print(unique_squares)  # {1, 4, 9, 16, 25}

