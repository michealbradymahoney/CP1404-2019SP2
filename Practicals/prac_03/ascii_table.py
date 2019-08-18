# Copy your ascii_table.py file from last week's prac into this week's folder.
# Create a function called get_number(lower, upper) to get a number, making sure that user input is numeric and
# within the given range.
# You can use exceptions to check the string is a valid number.
# Repeatedly re-prompt for a number until a valid one is entered, then return it.

LOWER = 33
UPPER = 127


def main():
    number = get_number_between()
    print("The character for {} is {}".format(number, chr(number)))


def get_number_between():
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    while number < LOWER or number > UPPER:
        number = int(
            input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    return number


main()
