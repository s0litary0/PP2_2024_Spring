def squares(a, b):
    num = a
    while num <= b:
        yield num ** 2
        num += 1

for i in squares(int(input()), int(input())):
    print(i, end = " ")
