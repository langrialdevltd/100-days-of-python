"""Day 3 exercise: Calculate the price of a pizza order."""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").strip().upper()
pepperoni = input("Do you want pepperoni? Y or N: ").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("That is not a valid pizza size.")
    raise SystemExit

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")
