import math

n_sides = float(input("Input number of sides:"))

side_length = float(input("Input the length of a side:"))

print("The area of the polygon is:", (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides)))