shot_status = {"sh001": "approved", "sh002": "pending", "sh003": "approved"}

# Unique shot IDs with approved status
approved_ids = {k for k, v in shot_status.items() if v == "approved"}
print(approved_ids)  # {'sh001', 'sh003'}
