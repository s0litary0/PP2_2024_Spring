#Example 1

a = {"apple", "pear", "banana"}
print(a)

#Unordered, Unchangeable, Dublicates not allowed

#Example 2

a = {1, 2, 3, True}
b = {0, 1, 2, False}
print(a, b, "\n")

#Example 3

a = set((1, 2, 3, 4, 5))

print(a)

#Example 4

set1 = {"apple", "banana", "cherry"}
for x in set1:
    print(x)

print("cherry" in set1)

#Example 5

a = {1, 2, 3}
b = {5, 6, 7}
a.add(4)
print(a)
a.update(b)
print(a)