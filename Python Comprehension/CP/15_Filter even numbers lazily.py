numbers = range(10)

# Generator: only even numbers
even_gen = (n for n in numbers if n % 2 == 0)

print(list(even_gen))  # [0, 2, 4, 6, 8]
