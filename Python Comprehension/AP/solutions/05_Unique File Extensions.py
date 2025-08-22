# Sample list of file names
files = [
    "render01.exr",
    "background.jpg",
    "mask.png",
    "comp_final.exr",
    "preview.jpg",
]

# Set comprehension - collect unique extensions
unique_exts = {f.split(".")[-1] for f in files}

# Print result
print("Unique Extensions:")
print(unique_exts)
