import random
def game():
    print("Hello! What is your name?")
    name = input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.\nTake a guess.")
    number = random.randrange(1, 21)
    guess = int(input())
    n = 0
    while guess != number:
        n += 1
        if guess > number: print("Your guess is too high.\nTake a guess.")
        if guess < number: print("Your guess is too low.\nTake a guess")
        guess = int(input())
    else:
        print("Good job, " + name + "! You guessed my number in", n + 1, "guesses!") 

game()