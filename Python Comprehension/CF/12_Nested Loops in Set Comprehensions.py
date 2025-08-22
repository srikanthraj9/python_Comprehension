# Without Comprehension

nums1 = [1, 2]
nums2 = [3, 4]

products = set()
for i in nums1:
    for j in nums2:
        products.add(i * j)

print(products)  # {3, 4, 6, 8}

# With set Comprehension

nums1 = [1, 2]
nums2 = [3, 4]

products = {i * j for i in nums1 for j in nums2}
print(products)

