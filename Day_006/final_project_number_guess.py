"""Day 6 final project: A simple number guessing game."""


def check_guess(guess, answer):
    if guess == answer:
        print("Correct!")
        return True
    elif guess > answer:
        print("Too high.")
    else:
        print("Too low.")

    return False


secret_number = 7
guess = 0
attempts = 0

print("Guess the secret number between 1 and 10.")

while guess != secret_number:
    guess = int(input("Make a guess: "))
    attempts += 1
    check_guess(guess, secret_number)

print(f"You guessed it in {attempts} attempts.")
