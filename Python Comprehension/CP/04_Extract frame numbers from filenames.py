files = ["sh001_1001.exr", "sh001_1002.exr", "sh002_1001.exr"]

# Extract frame numbers by splitting at "_"
frames = [f.split("_")[1].split(".")[0] for f in files]
print(frames)  # ['1001', '1002', '1001']
