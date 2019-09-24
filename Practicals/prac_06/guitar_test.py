from Practicals.prac_06.guitar import Guitar


name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)

guitarTwo = Guitar("Another Guitar", 2012)

print(guitar, "- Age = {} - Vintage = {}".format(guitar.get_age(), guitar.is_vintage()))
print(guitarTwo, "- Age = {} - Vintage = {}".format(guitarTwo.get_age(), guitarTwo.is_vintage()))
