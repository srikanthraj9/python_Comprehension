# Without comprehension

numbers = [1, 2, 3, 4, 5, 6]
even_squares = {}
for n in numbers:
    if n % 2 == 0:
        even_squares[n] = n**2
print(even_squares)

# With Dictionary comprehension

numbers = [1, 2, 3, 4, 5, 6]
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36}

