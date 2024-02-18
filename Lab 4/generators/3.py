def iter_3_4(n):
    num = 12
    while num <= n:
        yield num
        num += 12

for i in iter_3_4(100):
    print(i, end = " ")