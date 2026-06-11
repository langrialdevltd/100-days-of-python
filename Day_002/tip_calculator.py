"""Day 2 project: Tip calculator."""

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people will split the bill? "))

tip_as_decimal = tip_percentage / 100
total_bill = bill + (bill * tip_as_decimal)
amount_per_person = total_bill / number_of_people
final_amount = round(amount_per_person, 2)

print(f"Each person should pay: ${final_amount:.2f}")
