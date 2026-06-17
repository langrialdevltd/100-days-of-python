"""Day 6 challenge: Practice calling the same function many times."""


def make_step():
    print("Take one step forward")


def turn_corner():
    print("Turn left")
    print("Take one step forward")
    print("Turn right")


def walk_one_block():
    make_step()
    make_step()
    turn_corner()


print("Walking around the practice track:")

for block in range(4):
    print(f"\nBlock number {block + 1}")
    walk_one_block()

print("\nPractice complete!")
