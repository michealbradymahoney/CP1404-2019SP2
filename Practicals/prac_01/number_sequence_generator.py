# Menu-driven number sequence generator:
# A school teacher requires a small program that would allow primary school students to learn about
# various number sequences. The teacher is interested in a simple menu-driven program that has the following choices
# (where x and y are inputs the user enters once at the start of the program):
#
# i. Show the even numbers from x to y
# ii. Show the odd numbers from x to y
# iii. Show the squares from x to y
# iv. Exit the program
import math

menu = '\n*** MENU *** \n1 - Show the even numbers from x to y \n2 - Show the odd numbers from x to y\n' \
       '3 - Show the squares from x to y\nQ - Exit the program'
print(menu)
menu_choice = input(">>> ").upper()
while menu_choice != 'Q':
    try:
        if menu_choice == "1":
            x = int(input("What is the value of x?"))
            y = int(input("What is the value of y?"))
            for number in range(x + 1, y, 1):
                if number % 2 == 0:
                    print(number, end=' ')
        elif menu_choice == "2":
            x = int(input("What is the value of x?"))
            y = int(input("What is the value of y?"))
            for number in range(x + 1, y, 1):
                if number % 2 == 1:
                    print(number, end=' ')
        elif menu_choice == "3":
            x = int(input("What is the value of x?"))
            y = int(input("What is the value of y?"))
            for number in range(x + 1, y, 1):
                is_square_check = math.sqrt(number)
                if is_square_check.is_integer():
                    print(number, end=' ')
        else:
            print('Invalid Choice')
        print(menu)
        menu_choice = input(">>> ").upper()
    except ValueError:
        print("You must enter an integer")
print('Thank you for coming!')
