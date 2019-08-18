# Start new file, ascii_table.py, and write code for this program. Remember that you can use the ord() and chr()
# functions to convert characters to ASCII integer values and vice versa.

char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))
number = int(input("Enter a number between 33 and 127: "))
print("The character for {} is {}".format(number, chr(number)))
