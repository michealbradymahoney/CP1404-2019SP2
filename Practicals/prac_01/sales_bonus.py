"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Now write the Python code to complete the program according to that docstring.
# The first line might look like:
# sales = float(input("Enter sales: $"))
# Run and test the code with a few different values to verify that it works.
# Whenever you are testing code, you should not just use random values but values that you know the expected
# output for and that test all paths of execution, including the boundary or edge case.
# So, for this program we could use the following (we're only interested in the values, not the format):
#
# Test Input	Expected Output
# 500	             50
# 2000	            300
# 1000 (edge case)	150

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("Bonus is $", bonus, sep='')

# Add a loop to the sales bonus exercise you did above, so that the program repeatedly asks for the
# user's sales and prints the bonus until they enter a negative number.
# Remember that until is the opposite of while.

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus is $", bonus, sep='')
    sales = float(input("Enter sales: $"))