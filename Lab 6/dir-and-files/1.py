import os

# path = input()
path = "./"

print("Directories in", path, ":", end = " ")
with os.scandir(path) as it:
    for entry in it:
        if entry.is_dir():
            print(entry.name, end = " ")
print("\n")

print("Files and directories in", path, ":", end = " ")
with os.scandir(path) as it:
    for entry in it:
        print(entry.name, end = " ")
print("\n")

print("Files in", path, ":", end = " ")
with os.scandir(path) as it:
    for entry in it:
        if entry.is_file():
            print(entry.name, end = " ")