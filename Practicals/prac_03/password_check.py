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

MINIMUM_LENGTH = 5


def main():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    print('*' * len(password))


main()