# Menu-driven number sequence generator:
# A school teacher requires a small program that would allow primary school students to learn about
# various number sequences. The teacher is interested in a simple menu-driven program that has the following choices
# (where x and y are inputs the user enters once at the start of the program):
#
# i. Show the even numbers from x to y
# ii. Show the odd numbers from x to y
# iii. Show the squares from x to y
# iv. Exit the program

menu = '*** MENU *** \n1 - Show the even numbers from x to y \n2 - Show the odd numbers from x to y\n' \
       '3 - Show the squares from x to y\nQ - Exit the program'
print(menu)
menu_choice = input(">>> ").upper()
while menu_choice != 'Q':
    if menu_choice == 1:
        break
    elif menu_choice == 2:
        break
    elif menu_choice == 3:
        break
    else:
        print('Invalid Choice')
    print(menu)
    menu_choice = input(">>> ").upper()
print('Thank you for coming!')
