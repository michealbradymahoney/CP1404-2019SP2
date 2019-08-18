"""
Micheal Brady-Mahoney
"""
MINIMUM_LENGTH = 5

password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
while len(password) < MINIMUM_LENGTH:
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
print('*' * len(password))
