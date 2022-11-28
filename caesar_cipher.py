# Variables
text = 'none'
shift = 0
is_running = True


# Functions
def encrypt(txt, sh):
    enc_txt = list(txt)
    result = ""
    for v in enc_txt:
        if 97 <= ord(v) <= 122:
            new_v = chr(ord(v) + int(sh))
            if ord(new_v) > 122:
                new_v = chr(ord(new_v) - 26)
            result += new_v
        elif 65 <= ord(v) <= 90:
            new_v = chr(ord(v) + int(sh))
            if ord(new_v) > 90:
                new_v = chr(ord(new_v) - 26)
            result += new_v
        elif v in " 0123456789":
            new_v = v
            result += new_v

    return result


def decrypt(txt, sh):
    dec_txt = list(txt)
    result = ""
    for v in dec_txt:
        if 97 <= ord(v) <= 122:
            new_v = chr(ord(v) - int(sh))
            if ord(new_v) < 97:
                new_v = chr(ord(new_v) + 26)
            result += new_v
        elif 65 <= ord(v) <= 90:
            new_v = chr(ord(v) - int(sh))
            if ord(new_v) < 65:
                new_v = chr(ord(new_v) + 26)
            result += new_v
        elif v in " 0123456789":
            new_v = v
            result += new_v

    return result


def menu():
    print('Choose your action: ', '1.Encrypt', '2.Decrypt', '3.Exit', sep="\n")


# User Interaction
while is_running:
    menu()
    action = input()
    while action.isdigit() != 1:
        action = input('There is not such option, try again:')
    if action == '1':
        text = input("Give text to encrypt:")
        shift = input("Give shift:")
        while shift.isdigit() != 1:
            shift = input("Wrong value try again")
        shift = int(shift) % 26
        print(encrypt(text, shift))
    elif action == '2':
        text = input("Give text to decrypt:")
        shift = input("Give shift:")
        while shift.isdigit() != 1:
            shift = input("Wrong value try again")
        print(decrypt(text, shift))
    elif action == '3':
        is_running = False
    else:
        print('Invalid option, available options are [1 , 2 , 3 ]', '\n')
