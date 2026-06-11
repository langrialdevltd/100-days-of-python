"""Day 2: Number manipulation in Python."""

# Rounding a number
print(round(8 / 3))
print(round(8 / 3, 2))

# Floor division removes the decimal part.
print(8 // 3)

# Assignment operators update an existing value.
score = 0
score += 1
print(score)

score -= 1
print(score)

score += 5
score *= 2
score /= 2
print(score)

# F-strings combine values of different data types in one string.
name = "Raza"
height = 5.9
is_learning = True

print(f"My name is {name}.")
print(f"My score is {score}.")
print(f"My height is {height}, and learning Python is {is_learning}.")

# Format a number to two decimal places.
price = 12 / 7
print(f"The price is ${price:.2f}.")
