

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]

print(squares)   # [1, 4, 9, 16, 25]

# Generator Expression
numbers = [1, 2, 3, 4, 5]
squares_gen = (n**2 for n in numbers)

print(squares_gen)        # <generator object ...>
print(list(squares_gen))  # [1, 4, 9, 16, 25]