# Nested Loops in List Comprehensions

# Without Comprehension

nums1 = [1, 2]
nums2 = [10, 20]

pairs = []
for i in nums1:
    for j in nums2:
        pairs.append((i, j))

print(pairs)


# With List Comprehension
nums1 = [1, 2]
nums2 = [10, 20]

pairs = [(i, j) for i in nums1 for j in nums2]

print(pairs)


