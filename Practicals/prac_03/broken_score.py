"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# Debugging:
# Someone (it's not polite to say who) was trying to write a program to tell the user if their score is
# invalid, bad, passable or excellent, but their code is in the "bad" category and doesn't work.
# Rewrite the following programming attempt using the most efficient if-elif-else 'ladder' you can.
# The code is available here at: broken_score.py
# Remember to click Raw before copying and pasting so you get proper formatting!
# The intention is that the score must be between 0 and 100 inclusive; 90 or more is excellent;
# 50 or more is a pass; below 50 is bad.
# Be very careful of your boundary conditions... and test!

# use a function that takes in the score as a parameter and returns the result to be printed.
# The function should not print it; the main program should store and print the returned value.


def main():
    score = get_score()
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score


main()
