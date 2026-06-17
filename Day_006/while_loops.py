"""Day 6: While loops keep running while a condition is True."""


countdown = 5

while countdown > 0:
    print(f"Launching in {countdown}")
    countdown -= 1

print("Launch!")

print("\nWhile loops are useful when we do not know the exact number of repeats.")

battery = 3

while battery > 0:
    print("The toy car moves forward.")
    battery -= 1

print("The battery is empty.")
