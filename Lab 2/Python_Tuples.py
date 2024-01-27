#Example 1
thistuple = (1, 2, 3)
print(thistuple)
#Ordered, Unchangeable, Allow Duplicates

#Example 2
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
if "kiwi" in thistuple:
    print("Yes")

#Example 3
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Example 4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Example 5
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)