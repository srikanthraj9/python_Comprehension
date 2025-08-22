matrix = [[1, 2], [3, 4], [5, 6]]

# Flatten into single list
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
