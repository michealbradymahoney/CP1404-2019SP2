"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_celsius_to_fahrenheit(fahrenheit)
            print(celsius)
        elif choice == "F":
            celsius = float(input("Celsius: "))
            convert_fahrenheit_to_celsius(celsius)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
