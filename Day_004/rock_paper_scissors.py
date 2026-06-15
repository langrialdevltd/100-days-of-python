"""Day 4 project: Play Rock Paper Scissors against the computer."""

import random


ROCK = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [ROCK, PAPER, SCISSORS]
choice_names = ["Rock", "Paper", "Scissors"]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
)

if user_choice < 0 or user_choice > 2:
    print("That is not a valid choice. You lose!")
else:
    computer_choice = random.randint(0, 2)

    print(f"\nYou chose {choice_names[user_choice]}:")
    print(choices[user_choice])
    print(f"Computer chose {choice_names[computer_choice]}:")
    print(choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice - computer_choice) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")
