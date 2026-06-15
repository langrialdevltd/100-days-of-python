"""Day 4: Avoid index errors and create nested lists."""

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

number_of_fruits = len(fruits)
last_fruit = fruits[number_of_fruits - 1]

print(f"There are {number_of_fruits} fruits.")
print(f"The last fruit is {last_fruit}.")
print(dirty_dozen)
print(f"First vegetable: {dirty_dozen[1][0]}")

# Valid list indexes run from 0 through len(list) - 1.
# print(fruits[len(fruits)])  # Uncomment to see an IndexError.
