# Write a program using a dictionary instead of the above parallel lists that allows the user to enter the
# date-of-birth details for 5 people, and have it display their individual ages. Hint: you can split() a string like
# "12/4/1999", as we did in the lecture last week.

import re

date_separator = ('/', ' ', '-', '.', ',')
name_birth_dict = dict()

for i in range(0, 5):
    name = input("Enter a name: ")
    date_of_birth = input("Enter date of birth: ")
    date_of_birth = re.split("[%s]" % ("".join(date_separator)), date_of_birth)
    name_birth_dict[name] = date_of_birth

print(name_birth_dict)
