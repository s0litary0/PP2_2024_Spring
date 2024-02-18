def gen(n):
    num  = n
    while num != -1:
        yield num
        num -= 1

for i in gen(10):
    print(i, end = " ")