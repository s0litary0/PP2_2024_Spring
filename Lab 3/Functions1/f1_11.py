def ispalindrome(x):
    x = str(x)
    y = ""
    for i in range(len(x) - 1, -1, -1):
        y += x[i]

    if x == y:
        print("Yes")
    else:
        print("No")
ispalindrome(input())



