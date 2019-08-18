"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
# Write a program that asks for and validates a person's password.
# The program is not for comparing a password to a known password, but validating the 'strength' of a new password,
# like you see on websites: enter your password and then it tells you if it's valid (matches the required pattern)
# and re-prompts if it's not.
# All passwords must contain at least one each of: number, lowercase and uppercase character.
#
# The starter code uses constants (variables at the top of the code, named in ALL_CAPS) to store:
#
# a. the minimum and maximum length of the password
# b. whether or not a special character (not alphabetical or numerical) is required
#
# Remember when a program has constants, you should use them everywhere you can so that if you change them at the top,
# this change affects the whole program as expected.
# E.g. if you changed the minimum length to 5, the program should print 5 and should check to make sure the
# password is >= 5 characters long.


MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False
    # if we get here (without returning False), then the password must be valid
    return True


main()
