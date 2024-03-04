import os

def ABC_files_create():
    letter = ord('A')
    for i in range(26):
        file = open(chr(letter) + '.py', 'w')
        file.close()
        letter += 1

# ABC_files_create()

def ABC_files_delete():
    letter = ord('A')
    for i in range(26):
         os.remove(chr(letter) + '.py')
         letter += 1

# ABC_files_delete()