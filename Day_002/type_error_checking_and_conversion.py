"""Day 2: Type errors, type checking, and type conversion."""

name_length = len("Raza")

# This causes a TypeError because an integer cannot be joined to a string:
# print("Your name has " + name_length + " characters.")

# type() checks the data type of a value.
print(type(name_length))

# Convert an integer into a string.
name_length_as_string = str(name_length)
print("Your name has " + name_length_as_string + " characters.")

# Convert strings into numbers.
whole_number = int("25")
decimal_number = float("12.5")
print(whole_number)
print(decimal_number)

# Convert a number into a float.
print(float(100))

# input() returns a string, so it must be converted before doing arithmetic.
year_of_birth = input("What year were you born? ")
age_in_2026 = 2026 - int(year_of_birth)
print("You turn", age_in_2026, "years old in 2026.")
