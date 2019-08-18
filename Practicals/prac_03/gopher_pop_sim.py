"""
A secret population of 1000 gophers lives near the library. Every year, a random number of gophers is born,
between 10% of the current population, and 20%. (e.g. 15% of the gophers might give birth, increasing the
population by 150). Also each year, a random number of gophers die, between 5% and 25% (e.g. 8% of the
gophers might die, reducing the population by 80).

Write a program that simulates a population of gophers over a ten-year period and displays each year's
population size. The output should look something like this (it's random, so yours won't be the same):
"""

import random


print("Welcome to the Gopher Population Simulator!")
STARTING_POPULATION = 1000
total_population = 1000

print("Starting population:", STARTING_POPULATION)

year = 0
for year in range(10):
    gophers_born = round(random.uniform(0.10, 0.20) * 1000)
    gophers_died = round(random.uniform(0.05, 0.25) * 1000)
    total_population = STARTING_POPULATION + gophers_born - gophers_died
    print("Year", year+1, "\n")
    print("{} gophers were born. {} died\nPopulation:{}".format(gophers_born, gophers_died, total_population))


