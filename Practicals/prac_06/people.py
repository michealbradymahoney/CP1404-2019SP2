from Practicals.prac_06.person import Person

names = []
# first_name = input("first name: ")
# while first_name != "":
#     last_name = input("last name: ")
#     age = input("age: ")
#     new_person = Person(first_name, last_name, age)
#     names.append(new_person)
#     print("{} {} aged {} added".format(first_name, last_name, age))
#     first_name = input("first name: ")

names.append(Person("John", "Jones", 40))
names.append(Person("Jack", "Jones", 50))
names.append(Person("Mary", "Jones", 60))
names.append(Person("Jack", "Smith", 27))
names.sort()

names.sort()
print("These are the names:")
for i, person in enumerate(names, 1):
    print("{0}: First Name: {1.first_name} - Last Name: {1.last_name} - Age: {1.age}".format(i, person))
