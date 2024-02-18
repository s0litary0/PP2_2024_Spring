def gen(N):
    num = 0
    while num <= N:
        yield num ** 2
        num += 1

for i in gen(10):
    print(i, end = " ")