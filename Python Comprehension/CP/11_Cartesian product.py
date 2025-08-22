nums1 = [1, 2]
nums2 = [3, 4]

# All products, unique values only
products = {i * j for i in nums1 for j in nums2}
print(products)  # {3, 4, 6, 8}
