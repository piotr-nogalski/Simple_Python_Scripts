# KANTOR

# Currencies
zloty = 1
dollar_value = 4.54
euro_value = 4.70
dollar_to_euro = 0.97


# Functions


def exchange(c1, c2, value=1):
    # Zloty
    if c1 == '1' and c2 == '1':
        return value
    elif c1 == '1' and c2 == '2':
        return value / euro_value
    elif c1 == '1' and c2 == '3':
        return value / dollar_value
    # Euro
    elif c1 == '2' and c2 == '1':
        return value * euro_value
    elif c1 == '2' and c2 == '2':
        return value
    elif c1 == '2' and c2 == '3':
        return value * dollar_to_euro
    # Dollar
    elif c1 == '3' and c2 == '1':
        return value * dollar_value
    elif c1 == '3' and c2 == '2':
        return value / dollar_to_euro
    elif c1 == '3' and c2 == '3':
        return value


def print_currency(c):
    if c == '1':
        return 'PLN'
    elif c == '2':
        return 'EUR'
    elif c == '3':
        return 'USD'

# User Interactions


print("Welcome to cantor dear user, please select currency that you want to exchange")
print("1.PLN(1PLN)", "2.EUR(4.54PLN)", "3.USD(4.70PLN)", sep="\n")
curr = input()

while curr.isdigit() != 1 or int(curr) > 3:
    curr = input("This input is invalid try again: ")

print("What you want to exchange for?: ")
print("1.PLN(1 PLN)", "2.EUR(4.54 PLN)", "3.USD(4.70 PLN)", sep="\n")
curr_exch = input()

while curr_exch.isdigit() != 1 or int(curr_exch) > 3:
    curr_exch = input("This input is invalid try again: ")

cash = input("How much you want to exchange?(We accept only digit values):")

while cash.isdigit() != 1:
    cash = input('Wrong value, try again:')

print("Here is your", round(float(exchange(curr, curr_exch, int(cash))), 2), print_currency(curr_exch))
