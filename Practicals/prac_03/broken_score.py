"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    determine_status(score)


def determine_status(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        elif score > 90:
            print("Excellent")
        elif score > 50:
            print("Passable")
    if score < 50:
        print("Bad")


main()
