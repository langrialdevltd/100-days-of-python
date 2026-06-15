"""Day 4: Store, access, modify, and extend Python lists."""

states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]

print(f"First state: {states_of_america[0]}")
print(f"Last state: {states_of_america[-1]}")

states_of_america[1] = "Pencilvania"
states_of_america.append("Raza Land")
states_of_america.extend(["Khalid Land", "Python Land"])

print(states_of_america)


# Commonly used list methods
fruits = ["Apple", "Banana", "Cherry", "Banana"]
print(f"\nStarting list: {fruits}")

# append() adds one item to the end.
fruits.append("Orange")
print(f"After append(): {fruits}")

# extend() adds every item from another iterable.
fruits.extend(["Mango", "Peach"])
print(f"After extend(): {fruits}")

# insert() adds an item at a particular index.
fruits.insert(1, "Kiwi")
print(f"After insert(): {fruits}")

# remove() deletes the first matching value.
fruits.remove("Banana")
print(f"After remove(): {fruits}")

# pop() removes and returns an item. The default is the last item.
removed_fruit = fruits.pop()
print(f"pop() removed {removed_fruit}: {fruits}")

# index() returns the index of the first matching value.
cherry_index = fruits.index("Cherry")
print(f"Cherry is at index {cherry_index}.")

# count() returns how many times a value appears.
banana_count = fruits.count("Banana")
print(f"Banana appears {banana_count} time(s).")

# sort() changes the list into ascending order.
fruits.sort()
print(f"After sort(): {fruits}")

# reverse() reverses the current order.
fruits.reverse()
print(f"After reverse(): {fruits}")

# copy() creates a separate shallow copy of the list.
fruits_copy = fruits.copy()
fruits_copy.append("Watermelon")
print(f"Original list: {fruits}")
print(f"Copied list: {fruits_copy}")

# clear() removes every item from the list.
fruits_copy.clear()
print(f"After clear(): {fruits_copy}")
