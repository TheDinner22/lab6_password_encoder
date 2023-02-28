# Joe Goodman
# 02/28/23
# encode passwords and then decode them

# crash the program with a custom error message
# msg is a string
# this function returns nothing and will crash the program
def error(msg):
    raise Exception(msg)

# prints the menu plus whitespace, nothing returned
def print_menu():
    print("")
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

# get input after displaying the menu to the user
# the input should only ever be "1", "2", or "3"
#
# this function returns the input as a number 
# UNLESS
# the input is invalid, in which case the program crashes
def menu_input():
    user_input = int(input("Please enter an option: "))

    # if input is invalid, crash
    if user_input < 1 or user_input > 3:
        error("invalid input!!!")

    return user_input

def main():
    pass

if __name__ == "__main__":
    main()
