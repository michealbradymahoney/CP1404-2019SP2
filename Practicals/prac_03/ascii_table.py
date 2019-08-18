# Copy your ascii_table.py file from last week's prac into this week's folder.
# Create a function called get_number(lower, upper) to get a number, making sure that user input is numeric and
# within the given range.
# You can use exceptions to check the string is a valid number.
# Repeatedly re-prompt for a number until a valid one is entered, then return it.

LOWER = 33
UPPER = 127


def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    number = get_number_between(LOWER, UPPER)
    print("The character for {} is {}".format(number, chr(number)))

    for value in range(LOWER, UPPER + 1):
        print("{:3} {:>4}".format(value, chr(value)))


def get_number_between(lower, upper):
    number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
    while number < lower or number > upper:
        number = int(
            input("Enter a number between {} and {}: ".format(lower, upper)))
    return number


main()
