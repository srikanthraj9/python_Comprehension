files = ["sh001_1001.exr", "sh001_1002.exr", "sh002_1001.exr"]

# Generator for extracting frame numbers
frames_gen = (f.split("_")[1].split(".")[0] for f in files)

print(next(frames_gen))  # 1001
print(next(frames_gen))  # 1002
print(list(frames_gen))  # ['1001'] (remaining)