num_items = int(input("Number of items:"))
total = float(0)
while num_items < 0:
    print("Invalid number of items")
    num_items = int(input("Number of items:"))
else:
    for count in range (num_items):
        price = float(input("Price of item: "))
        total+=price
    if total > 100:
        total*=.9
    print("Total price for " + str(num_items) + " items is ${:.2f} ".format(total))