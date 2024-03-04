s = input("Check if string is palindrome:")

s_reversed = reversed(s)

if list(s) == list(s_reversed):
    print(s + " is palindrome")
else:
    print(s + " is not palindrome")