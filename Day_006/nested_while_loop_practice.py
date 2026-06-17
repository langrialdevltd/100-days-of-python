"""Day 6 challenge: Practice a while loop inside a function."""


def print_line(symbol, amount):
    count = 0

    while count < amount:
        print(symbol)
        count += 1


print("Small pattern practice")
print_line("*", 3)

print("\nBigger pattern practice")
print_line("#", 5)

print("\nDone practicing nested code blocks.")
