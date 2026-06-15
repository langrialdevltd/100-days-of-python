"""Day 4: Generate pseudorandom values with Python's random module."""

import random


random_integer = random.randint(1, 10)
print(f"Random integer from 1 to 10: {random_integer}")

random_number_0_to_1 = random.random()
print(f"Random float from 0.0 to 1.0: {random_number_0_to_1}")

random_float = random.uniform(1, 10)
print(f"Random float from 1.0 to 10.0: {random_float}")

coin_toss = random.randint(0, 1)
if coin_toss == 0:
    print("Heads")
else:
    print("Tails")
