
# This is just added so Python can read the module that is in the parent folder
import sys
import os
sys.path.append(os.path.abspath("./.."))

import random
from List import List

def switch_names(person:tuple[str, str])->(str, str):
    return (
        person[1],
        person[0],
    )

people = List()

# The names are used to generate some test data for the list program
names = open("names.txt", "r").read().split("\n")
names = filter(lambda x : x != "", names)
names = list(names)

# Generate some random people
for i in range(0, 5):
    first_name = random.choice(names)
    last_name = random.choice(names)

    person = (first_name, last_name)

    people.add(person)


# Print the people
print("Before name switch")
for person in people:
    print(person)


# Switch the names of the people with map
people = map(switch_names, people)
people = List(people)

# Print the people, but their first and last names are switched
print("\nAfter name switch")
for person in people:
    print(person)

