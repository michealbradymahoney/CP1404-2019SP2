# Create a version of the above electricity program that uses a dictionary to store the tariffs and the corresponding
# cost. In the prompt, list all of the tariffs (all of the dictionary keys) and make sure a valid one is selected.
# Use the appropriate cost from the dictionary to calculate the bill total.
#
# You will need to change how you present the "Which tariff" prompt, since these values come from the dictionary.
#
# To show the benefit of this, add three more tariffs (make them up).
# You should find that this is a very simple step for you, and your program can handle it without any extra coding.

tariff = 0
cents_per_kwh = 0
print("Electricity bill estimator 2.0")

TARIFFS = {11: 0.244618, 31: 0.136928}

while tariff != 11 and 31:
    try:
        tariff = int(input("Which tariff? 11 or 31: "))
        if tariff == 11:
            cents_per_kwh = TARIFFS[11]
        elif tariff == 31:
            cents_per_kwh = TARIFFS[31]
        else:
            print("Must be tariff 11 or 31")
    except ValueError:
        print("Must be a number, 11 or 31")
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days:"))
bill_total = cents_per_kwh * daily_use * billing_days
print('Estimated bill: ${:.2f}'.format(bill_total))
