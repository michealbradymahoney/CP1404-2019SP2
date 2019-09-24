from Practicals.prac_06.car import Car

MENU = "Menu: \n d) drive \n r) refuel \n q) quit"

print("Lets Drive!")
name = input("Car name:")

car = Car(name, 100)
print(car)

print(MENU)

choice = input("Enter your choice: ".lower())
while choice != "q":
    if choice == "d":
        drive_distance = int(input("How many km do you with to drive? "))
        while drive_distance < 0:
            print("Distance must be >= 0")
            drive_distance = int(input("How many km do you with to drive? "))
        distance_driven = car.drive(drive_distance)
        print("The car drove {}km".format(distance_driven))
        if car.fuel == 0:
            print("and ran out of fuel")
    elif choice == "r":
        adding_fuel = int(input("How many units of fuel do yuo want to add to the car?"))
        while adding_fuel < 0:
            print("Fuel amount must be >= 0")
            adding_fuel = int(input("How many units of fuel do yuo want to add to the car?"))
        car.add_fuel(adding_fuel)
        print("Added {} units of fuel".format(adding_fuel))
    else:
        print("Invalid choice")
    print("\n", car, "\n", MENU)
    choice = input("Enter your choice: ".lower())
print("\nGoodbye {}'s drive".format(car.name))

