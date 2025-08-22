# Sample frame ranges: (shot_name, start_frame, end_frame)
frame_ranges = [
    ("shot001", 1, 101),
    ("shot002", 50, 250),
    ("shot003", 200, 320),
    ("shot004", 100, 400),
]

# 1. List comprehension - filter shots with more than 150 frames
long_shots = [name for (name, start, end) in frame_ranges if (end - start) > 150]

# 2. Dictionary comprehension - calculate total frame count
frame_counts = {name: (end - start + 1) for (name, start, end) in frame_ranges}

# Print results
print("Shots with more than 150 frames:")
print(long_shots)

print("\nFrame Counts:")
print(frame_counts)
