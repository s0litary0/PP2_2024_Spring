'''x = int(input())
k = 0
for i in range(1, x + 1):
    if x % i == 0:
        k += 1

if k == 2:
    print("It's prime")
else:
    print("It's not prime")
'''
def func(j, *x):
    y = []
    while j != len(x):
        k = 0
        for i in range(1, int(x[j]) + 1):
            if int(x[j]) % i == 0:
                k += 1
        if k == 2:
            y.append(int(x[j]))
        j += 1

    return y

s = input()

print(func(0, *s.split(" ")))