# Start new file, ascii_table.py, and write code for this program. Remember that you can use the ord() and chr()
# functions to convert characters to ASCII integer values and vice versa.

# char = input("Enter a character: ")
# print("The ASCII code for {} is {}".format(char, ord(char)))
# number = int(input("Enter a number between 33 and 127: "))
# print("The character for {} is {}".format(number, chr(number)))

# Add error checking so that the number entered must be between the LOWER (33) and UPPER (127) bounds.
# Use constants for these values and use them in both your print statement and in your while loop condition.
# That is, the numbers 33 and 127 should appear only once.
# Use the str.format() method everywhere you print literals and variable values.

# LOWER = 33
# UPPER = 127
#
# char = input("Enter a character: ")
# print("The ASCII code for {} is {}".format(char, ord(char)))
# number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
# while number < LOWER or number > UPPER:
#     number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
# print("The character for {} is {}".format(number, chr(number)))

# Add on to this program by writing code that displays a table with two columns, one for the numeric
# ASCII value and the other for the character itself. Use the str.format() method to align the text nicely
# in two columns. Print the values between LOWER and UPPER.

# LOWER = 33
# UPPER = 127
#
# for value in range(LOWER, UPPER + 1):
#     print("{:3} {:>4}".format(value, chr(value)))

# Add columns to your ASCII table output. Ask the user for how many columns to print,
# then figure out how to write loop(s) and print statements to achieve this.

LOWER = 33
UPPER = 127

columns = int(input("Enter number of columns: "))
number_of_values = UPPER - LOWER + 1
rows = number_of_values // columns
value = LOWER
for row in range(rows):
    for column in range(columns):
        print("{:6} {:>2}".format(value, chr(value)), end="")
        value += 1
    print()
