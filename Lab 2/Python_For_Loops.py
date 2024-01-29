#Example 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Example 2

for x in "banana":
  print(x)

#Example 3

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Example 4

for x in range(6):
  print(x)

#Example 5

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Example 6

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
