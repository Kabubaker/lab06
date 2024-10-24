"""
Kadeeja Abubaker
Emma DeNunzio
"""
def encoder(password):
    list = []
    list.extend(password)
    num = 0
    new_str = ""

    for i in list:
        num = (int(i) + 3) % 10
        new_str += str(num)

    return new_str

def decoder(encoded_password):
    list = []
    list.extend(encoded_password)
    num = 0
    original_str = ""

    for i in list:
        num = (int(i) - 3) % 10
        original_str += str(num)

    return original_str

def main():
    new_password = ""
    password = ""

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            new_password = encoder(password)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            if new_password:
                original_password = decoder(new_password)
                print(f"The encoded password is {new_password}, and the original password is {original_password}.\n")
            else:
                print("No password has been encoded yet.\n")

        elif option == 3:
            break

        else:
            print("Invalid option. Please try again.\n")

if __name__ == '__main__':
    main()
