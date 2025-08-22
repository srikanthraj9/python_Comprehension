numbers = [1, 2, 3, 4, 5]

# Generator for squares
squares_gen = (n * n for n in numbers)

print(squares_gen)        # <generator object ...>
print(list(squares_gen))  # [1, 4, 9, 16, 25]
