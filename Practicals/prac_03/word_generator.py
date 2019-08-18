"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""

# Get the word format from the user so they can customise it. Convert it to lowercase using a str method.

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word = ""
word_format = input("Enter word format using c for consonant and v for vowel: ")
word_format = word_format.lower()

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == "v":
        word += random.choice(VOWELS)
print(word)

