"""
Micheal Brady-Mahoney
"""
# MINIMUM_LENGTH = 5
#
# password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
# while len(password) < MINIMUM_LENGTH:
#     password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
# print('*' * len(password))

# Move all of the code inside a main() function and call main() at the bottom.
# Note: if you don't have a main function, the refactoring below will use global variables.
# So, it's an important first step to use main before adding other functions.

# MINIMUM_LENGTH = 5
#
#
# def main():
#     password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
#     while len(password) < MINIMUM_LENGTH:
#         password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
#     print('*' * len(password))
#
#
# main()

# Refactor the part that gets the password into a separate function...
# You can either do this manually, or by using PyCharm's refactoring tool.
# If you want to use the tool, select the lines that get and check the name (it should be 3-4 lines)
# then right-click (or use the main menu) and choose Refactor > Extract > Method...
# Change the name to get_password and press OK.
# PyCharm should create the function and replace the old code with a call to it like password = get_password()
# (Note that the details depend on how you wrote the code to start with.)

MINIMUM_LENGTH = 5


def main():
    password = get_password()
    print('*' * len(password))


def get_password():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    return password


main()
