#Example 1

a = {
    1 : 2,
    3 : 4
}
print(a)
print(a[1])
#Ordered, Changeable, Duplicates not allowed

#Example 2

cars = {
    "Mustang": ["v6", "v8"],
    "Color": {"red", "blue", "green"}
}

print(cars, "\n", cars["Color"])

#Example 3

thisdict = dict(name = "John", age = 35)
print(thisdict)

#Example 4

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

#Example 5

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)