def even_gen(n):
    num = 0
    while num <= n:
        yield num
        num += 2

a = int(input())
for i in even_gen(a):
    print(i, end = ", ")