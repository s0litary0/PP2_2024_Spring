def solve(numheads, numlegs):
    print("Rabbits:", int((numlegs - 2 * numheads) / 2))
    print("Chickens:", int(numheads - (numlegs - 2 * numheads) / 2))

solve(35, 94)