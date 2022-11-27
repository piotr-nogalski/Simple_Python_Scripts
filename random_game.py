# GRA LOSOWA

# Modules
import random
# Variables
random_number = random.randrange(1, 20)
# Functions


def take_number():
    value = input('Please give number from range 1-20: ')
    while not value.isdigit():
        value = input("Wrong input please try again!: ")
    user_number = int(value)
    return user_number


print(random_number)
print('Welcome to random game !')
guess = take_number()
# Game loop
while guess != random_number:
    if 1 <= guess <= 20:

        print("That's not the number")
        dec = input("Do you want to try again ?(y/n)")
        if dec == "y" or dec == "Y":

            guess = take_number()

        elif dec == "n" or dec == "N":

            guess = random_number
            print("Im sorry have a good day :/")

    else:
        print("This number is to high! Choose number in range 1-20!")
        dec = input("Do you want to try again ?(y/n)")

        if dec == "y" or dec == "Y":

            guess = take_number()

        elif dec == "n" or dec == "N":

            guess = random_number
            print("Im sorry have a good day :/")

print('The number was ' + str(random_number))
