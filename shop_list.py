# Variables
shop_list = []
is_running = True


# Functions
def add_product(a='product'):
    a.lower()
    shop_list.append(a)
    if len(shop_list) > 10:
        print("Max size of list is 10, you need to remove something !")
        shop_list.remove(a)


def remove_product(a='product'):
    a.lower()
    shop_list.remove(a)


def show_list():
    i = 1
    for v in shop_list:
        print(i, v)
        i += 1
    print('\n')


def menu():
    print('Choose your action: ', '1.Add Product', '2.Remove Product', '3.Show list', '4.Exit', sep="\n")


# User interaction
while is_running:
    menu()
    action = input()
    while action.isdigit() != 1:
        action = input('There is not such option, try again:')
        menu()
    if action == '1':
        product = input('Give product to add: ')
        add_product(product)
    elif action == '2':
        product = input('Give product to remove: ')
        try:
            remove_product(product)
        except ValueError:
            print('There is no such product !', '\n')
    elif action == '3':
        show_list()
    elif action == '4':
        is_running = False
