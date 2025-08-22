numbers = [1, 2, 2, 3, 4, 4, 5]

# Keep only unique squares
unique_squares = {n * n for n in numbers}
print(unique_squares)  # {1, 4, 9, 16, 25}