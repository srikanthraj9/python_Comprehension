shot_status = {"sh001": "approved", "sh002": "pending", "sh003": "approved"}

# Keep only approved ones
approved = {k: v for k, v in shot_status.items() if v == "approved"}
print(approved)  # {'sh001': 'approved', 'sh003': 'approved'}