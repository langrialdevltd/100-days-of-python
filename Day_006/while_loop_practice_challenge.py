"""Day 6 challenge: Use a while loop when the repeat count can change."""


def drink_water():
    print("Drink one glass of water")


glasses_goal = 5
glasses_finished = 0

while glasses_finished < glasses_goal:
    drink_water()
    glasses_finished += 1
    print(f"Glasses finished: {glasses_finished}")

print("Water goal completed!")
