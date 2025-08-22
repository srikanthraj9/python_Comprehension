# Sample asset data: (asset_name, asset_type)
assets = [
    ("tree", "prop"),
    ("car", "prop"),
    ("dragon", "character"),
    ("warrior", "character"),
]

# 1. List comprehension - filter only character assets
character_assets = [name for (name, a_type) in assets if a_type == "character"]

# 2. Dictionary comprehension - map asset name to its length
asset_name_lengths = {name: len(name) for (name, a_type) in assets}

# Print results
print("Character Assets:")
print(character_assets)

print("\nAsset Name Lengths:")
print(asset_name_lengths)
