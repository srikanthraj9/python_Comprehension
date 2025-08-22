files = ["sh001.exr", "sh002.exr", "sh003.exr"]

# Generator to yield filenames in uppercase
file_gen = (f.upper() for f in files)

for f in file_gen:

    print(f)
# output
# SH001.EXR
# SH002.EXR
# SH003.EXR
