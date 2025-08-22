# Sample list of file names
files = [
    "render01.exr",
    "background.jpg",
    "mask.png",
    "comp_final.exr",
]

# 1. List comprehension - filter only .exr files
exr_files = [f for f in files if f.endswith(".exr")]

# 2. Dictionary comprehension - map file to its extension
file_extensions = {f: f.split(".")[-1] for f in files}

# Print results
print("EXR Files:")
print(exr_files)

print("\nFile Extensions:")
print(file_extensions)
