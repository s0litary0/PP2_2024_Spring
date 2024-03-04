import os
path = input()

if os.access(path, os.F_OK):
    print("File name:", os.path.basename(path))
    print("Diretory:", os.path.dirname(path))