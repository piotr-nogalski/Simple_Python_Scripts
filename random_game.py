# Modules
import random


# Variables

random_number = random.randrange(17)
guessed_number = 0
guessed = "Good job " + str(random_number) + " is the number I was thinking about!"

# Welcome print

print("Hi, welcome to my game, try to guess what number Im thinking about in range 0 - 17")

# Function

while guessed_number != random_number:
    # Try / except is used for case where user gives letters or strings as an input
    try:
        guessed_number = int(input("Try to guess !:"))
        if guessed_number != random_number:
            print("That's not it !")
        else:
            print(guessed)
    except ValueError:
        print("That's not correct, try again")
