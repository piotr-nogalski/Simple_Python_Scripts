# Modules
import random


# Randomizer
def ran_val():
    value = random.randrange(0, 10)
    return int(value)


# Variables
resources = {'wood': ran_val(), 'stone': ran_val(), 'gold': ran_val(), 'silver': ran_val(), 'copper': ran_val()}
is_running = True


# Functions
def print_dict():
    for key in resources.keys():
        print(key, "->", resources[key])
    print()


def use_res(res):
    if res in resources:
        if resources[res] > 0:
            resources[res] = (resources[res] - 1)
            print("You have used", res)
            print()
        else:
            print("You have no", res, '!', '\n')
    else:
        print('There is no such resource!', '\n')


def menu():
    print('Choose your action: ', '1.List resources', '2.Use resources', '3.Exit', sep="\n")


# User interaction
while is_running:
    menu()
    action = input()
    while action.isdigit() != 1:
        action = input('There is not such option, try again:')
        menu()
    if action == '1':
        print_dict()
    elif action == '2':
        re = input("Choose resource:")
        use_res(re)
    elif action == '3':
        is_running = False
    else:
        print('Invalid option, available options are [1 , 2 , 3 ]', '\n')
