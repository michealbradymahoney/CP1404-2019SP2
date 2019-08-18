# Create an electricity bill estimator
# Inputs should be:
#
# - price per kWh in cents,
# - daily use in kWh, and
# - number of days in the billing period.
#
# Example use:
#
# Electricity bill estimator
# Enter cents per kWh: 35
# Enter daily use in kWh: 4.5
# Enter number of billing days: 90
# Estimated bill: $141.75

# print("Electricity bill estimator")
# cents_per_kwh = int(input("Enter cents per kWh: "))
# daily_use = float(input("Enter daily use in kWh: "))
# billing_days = int(input("Enter number of billing days:"))
# bill_total = cents_per_kwh * daily_use * billing_days / 100
# print("Estimated bill: $", bill_total, sep="")

# 2. Modify your bill estimator by asking the user to choose which tariff they are using -
# then use the appropriate stored value for cents per kWh.
# Start by defining two constants like below.
# Constants in Python are just variables written in ALL_CAPITALS.
# TARIFF_11 = 0.244618
# TARIFF_31 = 0.136928
# Example use:
#
# Electricity bill estimator 2.0
# Which tariff? 11 or 31: 11
# Enter daily use in kWh: 13.4
# Enter number of billing days: 90
# Estimated bill: $295.01


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = 0
print("Electricity bill estimator")
while tariff != 11 and 31:
    try:
        tariff = int(input("Which tariff? 11 or 31: "))
        if tariff == 11:
            cents_per_kwh = TARIFF_11
        elif tariff == 31:
            cents_per_kwh = TARIFF_31
        else:
            print("Must be tariff 11 or 31")
    except ValueError:
        print("Must be a number, 11 or 31")
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days:"))
bill_total = cents_per_kwh * daily_use * billing_days
print('Estimated bill: ${:.2f}'.format(bill_total))
