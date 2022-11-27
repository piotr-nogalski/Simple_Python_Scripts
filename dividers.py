# DZIELNIKI

# Variables
value = input("Please give number in range 0-100: ")

while not value.isdigit():
    value = input("Wrong input please try again: ")

number = int(value)
arr = [1]

# Divisors search algorithm
if 0 < number <= 100:

    for i in range(2, (number + 1)):

        if number % i == 0:
            arr.append(i)

    print("The divisors of " + str(number) + " are:")
    arr.reverse()
    print(arr)

elif number == 0:
    print("You can devise zero by every number :D")

else:
    print("You gave the wrong number, program will close")
