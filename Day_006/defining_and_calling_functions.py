"""Day 6: Defining and calling Python functions."""


def greet():
    print("Hello")
    print("Welcome to Day 6")
    print("Let's learn functions")


def make_tea():
    print("Boil water")
    print("Add tea bag")
    print("Pour water into the cup")
    print("Wait for the tea to brew")
    print("Add milk or sugar if you like")


print("Built-in functions can do work for us:")
name = "Python"
number_of_letters = len(name)
print(number_of_letters)

print("\nNow we call our own function:")
greet()

print("\nA function can bundle repeated instructions:")
make_tea()
