"""Day 3 project: Treasure Island."""

print(
    r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input(
    'You are at a crossroad. Type "left" or "right": '
).strip().lower()

if direction == "left":
    lake_choice = input(
        'You reach a lake. Type "wait" for a boat or "swim" across: '
    ).strip().lower()

    if lake_choice == "wait":
        door = input(
            "You arrive safely and find three doors. "
            'Choose "red", "yellow", or "blue": '
        ).strip().lower()

        if door == "red":
            print("The room is full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure. You Win!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("That door does not exist. Game Over.")
    else:
        print("You are attacked by an angry trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")
