#Example 1
thislist = [1, 2, 3]
print(thislist, len(thislist))
print(type(thislist))
thatlist = list((4, 5, 6))
print(thatlist)
#Ordered, changeable, allow dublicates

#Example 2
thislist = ["pen", "book", "pencil", "notebook", "eraser"]
print(thislist[0])
print(thislist[-1])
print(thislist[1:4], "\n")

#Example 3
if "pencil" in thislist:
    print("Yes")
if "money" in thislist:
    print("No")
print("\n")

#Example 4
thislist = ["pen", "book", "pencil", "notebook", "eraser"]
thislist[1] = "paper"
print(thislist)
thislist[1:4] = ["paper"]
print(thislist)
thislist.insert(1, "book")
print(thislist, "\n")

#Example 5
thislist = ["red", "blue", "yellow"]
thatlist = ["purple", "orange"]
thislist.append("green")
print(thislist)
thislist.extend(thatlist)
print(thislist)