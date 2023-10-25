# Lab 6: Version Control 28
# UF COP3502C Fall 2023
# Encoder: Luke Xue
# Decoder: Jessica Doten


def menu():
    """Menu function for selecting an option"""
    selection = None
    in_menu = True
    while in_menu:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')
        try:
            selection = int(input('Please enter an option: '))
        except:
            print('Invalid selection!\n')
            continue
        in_menu = False
    return selection


def encode(pw):
    """Function for encoding password"""
    encoded_pw = ''
    for i in pw:
        encoded_pw += str((int(i) + 3)%10)
    return encoded_pw


def decode(pw):
    """Function for decoding password"""
    decoded_pw = ''
    for i in pw:
        decoded_pw = decoded_pw + str((int(i) - 3)%10)
    return decoded_pw


"""Main body of program for encoding/decoding password"""
encoding = True
password = ''
encoded_pw = ''

while encoding:
    selection = menu()
    if selection == 1:
        password = input('Please enter your password to encode: ')
        encoded_pw = encode(password)
        print('Your password has been encoded and stored!\n')
    elif selection == 2:
        decoded_pw = decode(encoded_pw)
        print(f'The encoded password is {encoded_pw}, and the original password is {decoded_pw}')
    elif selection == 3:
        break
    else:
        print('Invalid selection!\n')
        continue