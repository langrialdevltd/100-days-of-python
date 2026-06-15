"""Day 4 exercise: Randomly choose who pays the bill."""

import random


friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

person_paying = random.choice(friends)
print(f"{person_paying} is going to buy the meal today!")

# The same result can be produced by choosing a random valid index.
random_index = random.randint(0, len(friends) - 1)
print(f"Using an index: {friends[random_index]} is paying.")
