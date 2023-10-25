def encode(pwd):
    new_pwd = ""
    for x in pwd:
        if int(x) >= 7:
            new_pwd += str(int(x)+3-10)
        else:
            new_pwd += str(int(x)+3)
    return new_pwd

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
            encode(pwd)
            print("Your password has been encoded and stored!")