"""Day 3: Use modulo to check whether a number is even or odd."""

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
