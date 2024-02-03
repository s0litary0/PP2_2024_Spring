def func(s):
    a = s.split(" ")
    a.reverse()
    for i in range(len(a)):
        print(a[i], end = ' ')

s1 = input()
func(s1)
