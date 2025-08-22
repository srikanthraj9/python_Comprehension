
# Without comprehension

numbers = [1, 2, 3, 4, 5, 6]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)

# With List  comprehension

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]

print(evens)  # [2, 4, 6]

