"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
MINIMUM_LENGTH = 4


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()
