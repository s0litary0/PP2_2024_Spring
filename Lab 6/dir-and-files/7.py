file1 = open('7.py', 'r')
file2 = open('7_copy.py', 'a')

for row in file1:
    file2.write(row)