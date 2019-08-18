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

print("Electricity bill estimator")
cents_per_kwh = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days:"))
bill_total = cents_per_kwh * daily_use * billing_days / 100
print("Estimated bill: $", bill_total, sep="")
