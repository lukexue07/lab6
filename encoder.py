# Lab 6: Version Control 28
# UF COP3502C Fall 2023
# Encoder: Luke Xue
# Decoder: Jessica Doten


def encode(pwd):
    new_pwd = ""
    for x in pwd:
        if int(x) >= 7:
            new_pwd += str(int(x)+3-10)
        else:
            new_pwd += str(int(x)+3)
    return new_pwd

def decode(pwd):
    decoded_pwd = ""
    for x in pwd:
        decoded_pwd = decoded_pwd + str((int(x)-3)%10)
    return decoded_pwd


if __name__ == "__main__":
    while True:
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        response = input("Please enter an option: ")
        if response == "1":
            pwd = input("Please enter your password to encode: ")
            new_pwd = encode(pwd)
            print("Your password has been encoded and stored!")

        if response == "2":
            decoded_pwd = decode(pwd)
            print(f'The encoded password is {new_pwd}, and the original password is {pwd}')

        if response == "3":
            break

        else:
            print("Invalid selection!\n")