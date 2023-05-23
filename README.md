# A quick List library

This is a really simple list library. It implements a list-like object with 
recursion, but it doesn't use recursion, so there are no worries about it 
hitting the recursion limit. 

## Examples

```python
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
```

