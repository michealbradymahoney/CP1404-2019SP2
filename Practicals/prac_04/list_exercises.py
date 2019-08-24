# Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
# The program should then output various interesting things, as in the output below.
# Note that you can use the functions min, max, sum and len, and you can use the append method to add a
# number to a list.
#
# Number: 5
# Number: 20
# Number: 1
# Number: 2
# Number: 3
# The first number is 5
# The last number is 3
# The smallest number is 1
# The largest number is 20
# The average of the numbers is 6.2

NUMS_TO_GET = 5
numbers = []
for i in range(NUMS_TO_GET):
    entered_number = int(input("Number:"))
    numbers.append(entered_number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))

# Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
entered_username = input("Enter username: ")
if entered_username in usernames:
    print("Access granted")
else:
    print("Access denied")
