files = ["sh001_v1.exr", "sh001_v2.exr", "sh002_v1.exr"]

# Build dict: shot → latest version
latest = {f.split("_")[0]: f.split("_")[1].split(".")[0] for f in files}
print(latest)  # {'sh001': 'v2', 'sh002': 'v1'}