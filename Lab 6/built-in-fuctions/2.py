s = input()

upperCase, lowerCase = 0, 0
for i in s:
    if i.isupper():
        upperCase += 1
    if i.islower():
        lowerCase += 1

print(f"Upper Case letters: {upperCase}\nLower Case letters: {lowerCase}")