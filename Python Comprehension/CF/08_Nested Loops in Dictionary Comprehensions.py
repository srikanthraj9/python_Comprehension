# Without Comprehension
nums1 = [1, 2]
nums2 = [10, 20]

result = {}
for i in nums1:           # outer loop
    for j in nums2:       # inner loop
        result[(i, j)] = i * j

print(result)

# With Dictionary Comprehension
nums1 = [1, 2]
nums2 = [10, 20]

pairs_dict = {i: j for i in nums1 for j in nums2}
print(pairs_dict)

