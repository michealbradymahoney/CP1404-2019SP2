"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")

# Questions
#
# When will a ValueError occur? When they are not a number
# When will a ZeroDivisionError occur? When trying to divide by zero
# Could you change the code to avoid the possibility of a ZeroDivisionError? You can add while True
# If you could figure out the answer to question 3, then make this change now.