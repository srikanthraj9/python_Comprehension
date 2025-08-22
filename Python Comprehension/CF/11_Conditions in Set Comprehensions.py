# Without comprehension:
numbers = [1, 2, 3, 4, 5, 6]
even_squares = set()
for n in numbers:
    if n % 2 == 0:
        even_squares.add(n**2)

print(even_squares)  # {4, 16, 36}

# With set comprehension:
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {n**2 for n in numbers if n % 2 == 0}

print(even_squares)  