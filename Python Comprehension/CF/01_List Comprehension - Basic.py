# Without List Comprehension

squares = []
for i in range(5):
    squares.append(i * i)

print(squares)
# Output: [0, 1, 4, 9, 16]



# With List Comprehension

squares = [i * i for i in range(5)]

print(squares)
# Output: [0, 1, 4, 9, 16]

