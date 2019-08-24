import random

MAX_NUMBER = 45
MIN_NUMBER = 1
NUMS_PER_GAME = 6

num_games = int(input("How many quick picks"))

for i in range(num_games):
    picks = []
    for j in range(NUMS_PER_GAME):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in picks:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        picks.append(number)
    picks.sort()
    print(" ".join("{:3}".format(number) for number in picks))
