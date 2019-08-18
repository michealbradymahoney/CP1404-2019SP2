# Shop Calculator
# A shop requires a small program that would allow them to quickly work out the total price for a number of items,
# each with different prices.
#
# The program allows the user to enter the number of items and the price of each different item.
# Then the program computes and displays the total price of those items.
# If the total price is over $100, then a 10% discount is applied to that total before the amount is
# displayed on the screen.
#
# The output should look something like (bold text represents user input):
#
# Number of items: 3
# Price of item: 100
# Price of item: 35.56
# Price of item: 3.24
# Total price for 3 items is $124.92
# Create the file shop_calculator.py and write this program.
# Note: start with the main logic, then adjust your program to improve the formatting if you need to.
# Note that the example output above uses string formatting to set the currency to 2 decimal places...
# don't worry about this for now... or do :)
#
# + Error checking (input validation loop):
# (Do this after you have completed the above program.) If the number of items is less than zero,
# the message "Invalid number of items!" should be displayed and this quantity must be re-entered by the user until
# it is valid.

num_items = int(input("Number of items: "))
total = 0
for i in range(num_items):
    price = float(input("Price of item: "))
    total += price
print("Total price for {} items is ${:.2f}".format(num_items, total))
