# POLA

# Modules
import math

# Functions


def check_values(a, b, c='1'):
    return a.isdigit() and b.isdigit() and c.isdigit()


def check_triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False


def check_rectangle(a, b):
    if a != 0 and b != 0:
        return True
    else:
        return False


def triangle_area(a, b, c):
    # s -> half of a perimeter
    s = ((a + b + c)/2)
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))
    return area


def rectangle_area(a, b):
    area = a*b
    return area


# User interactions
print("Welcome, choose your figure:", "1.Rectangle", "2.Triangle", sep="\n")
decision = input()

while decision.isdigit() != 1 or int(decision) > 2:
    decision = input("Your input is invalid please try again (Valid input is 1 or 2)")

if int(decision) == 1:
    val_x = input("Give the size of a first side: ")
    val_y = input("Give the size of a second side: ")

    while check_values(val_x, val_y) != 1 or check_rectangle(int(val_x), int(val_y)) != 1:
        print("That's not correct try again")
        val_x = input("Give the size of a first side: ")
        val_y = input("Give the size of a second side: ")

    print("Area of given rectangle is ", rectangle_area(int(val_x), int(val_y)))

elif int(decision) == 2:
    val_x = input("Give the size of a first side: ")
    val_y = input("Give the size of a second side: ")
    val_z = input("Give the size of a third side: ")

    while check_values(val_x, val_y, val_z) != 1 or check_triangle(int(val_x), int(val_y), int(val_z)) != 1:
        print("That's not correct try again")
        val_x = input("Give the size of a first side: ")
        val_y = input("Give the size of a second side: ")
        val_z = input("Give the size of a third side: ")

    print("Area of given triangle is ", triangle_area(int(val_x), int(val_y), int(val_z)))
