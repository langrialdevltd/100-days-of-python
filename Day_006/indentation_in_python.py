"""Day 6: Indentation shows which lines belong to a code block."""


def check_weather(sky):
    print("Checking the weather...")

    if sky == "clear":
        print("Wear sunglasses")
        print("Go for a walk")
    elif sky == "rainy":
        print("Take an umbrella")
        print("Wear waterproof shoes")
    else:
        print("Check again later")

    print("Weather check finished")


check_weather("clear")

print("\nThis print is outside the function because it is not indented.")
