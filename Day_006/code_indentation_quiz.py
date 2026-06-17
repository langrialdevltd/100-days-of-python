"""Day 6 quiz: Predict what each indentation example will print."""


print("Question 1")


def say_hello():
    print("Hello")
    print("World")


say_hello()

print("\nQuestion 2")


def check_score(score):
    if score > 80:
        print("Great score")
        print("You passed")
    else:
        print("Keep practicing")


check_score(92)

print("\nQuestion 3")


def pack_bag(has_homework):
    print("Put notebook in bag")

    if has_homework:
        print("Put homework in bag")

    print("Zip the bag")


pack_bag(True)
