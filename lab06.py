
"""
Kadeeja Abubaker
"""
def encoder(password):

    list = []

    list.extend(password)

    num = 0
    new_str = ""

    for i in list:
        num = int(i) + 3
        new_str += str(num)

    return new_str



def main():


    while True:
        print("Menu")
        print("-------------")

        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = int(input("Please enter an option: "))


        if option == 1:
            password = input("Please enter your password to encode: ")

            print("Your password has been encoded and stored!\n")

            new_password = encoder(password)


        if option == 2:
            print(f"The encoded password is {new_password}, and the original password is {password}.\n")

        if option == 3:
            break







if __name__ == '__main__':

    main()






