
# This is just added so Python can read the module that is in the parent folder
import sys
import os
sys.path.append(os.path.abspath("./.."))

from random import randrange
from List import List

numbers = List()

# Generate 100 random numbers
for _ in range(0, 100):
    numbers.add(randrange(0, 100))


# Remove the second number from the list
numbers.remove(1)

# Add 8 to the list
numbers.add(8)

# Remove all uneven numbers
numbers = filter(lambda x : x % 2 == 0, numbers)
numbers = List(numbers)


# Iterate through the numbers
for random_number in numbers:
    print(random_number)

# Print the numbers like a normal list
print(numbers)
