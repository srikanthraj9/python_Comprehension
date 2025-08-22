status_map = {"approved": 1, "pending": 2, "rendered": 3}

# Reverse mapping
rev_map = {v: k for k, v in status_map.items()}
print(rev_map)  # {1: 'approved', 2: 'pending', 3: 'rendered'}