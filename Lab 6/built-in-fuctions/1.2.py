product = 1

def f(a):
    global product
    product *= a
    return a

l = [1, 2, 3, 4, 5]

list(map(f, l))

print(product)