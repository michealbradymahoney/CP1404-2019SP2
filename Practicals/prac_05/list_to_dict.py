# Write a program using a dictionary instead of the above parallel lists that allows the user to enter the
# date-of-birth details for 5 people, and have it display their individual ages. Hint: you can split() a string like
# "12/4/1999", as we did in the lecture last week.

# import re
#
# date_separator = ('/', ' ', '-', '.', ',')
# name_birth_dict = dict()
#
# for i in range(0, 5):
#     name = input("Enter a name: ")
#     date_of_birth = input("Enter date of birth: ")
#     date_of_birth = re.split("[%s]" % ("".join(date_separator)), date_of_birth)
#     name_birth_dict[name] = date_of_birth
#
# print(name_birth_dict)

# Write a function that takes two parallel lists as input parameters and returns a dictionary where keys are from the
# first list and the values are from the second. Use the above example as a test case.

names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

names_dict = dict(zip(names, dates_of_birth))
print(names_dict)
