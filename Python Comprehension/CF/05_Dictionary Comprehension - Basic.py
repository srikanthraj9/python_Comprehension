# without dictionary comprehension:

squares = {}   # empty dictionary

for x in range(1, 6):
    squares[x] = x**2   # add key-value pair

print(squares)

# with dictionary comprehension

# Create a dictionary where keys are numbers 1–5 and values are their squares
squares = {x: x**2 for x in range(1, 6)}

print(squares)


