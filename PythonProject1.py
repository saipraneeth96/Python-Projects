# ROCK PAPER SCISSORS GAME
"""
WINNING CRITERIA:
1. Scissor wins against Paper
2. Paper wins against Rock
3. Rock wins against Scissor
"""
# importing random module
import random

# taking users and computers choice
user_choice = int(input("Enter your choice:\n "
                        "1. Type 0 for Rock \n "
                        "2. Type 1 for Paper \n "
                        "3. Type 2 for Scissors \n "
                        "Enter your choice: "))
computer_choice = random.randint(0, 2)

# checking if users choice is valid or not
if 2 < user_choice < 0:
    print("You entered choice invalid choice: YOU LOOSE")

# Displaying computer results
print(f"Computer choice {computer_choice}")

# finding the outcomes
if computer_choice == user_choice:
    print("It is a Draw")
elif computer_choice == 0 and user_choice == 2:
    print("You lost")
elif user_choice == 0 and computer_choice == 2:
    print("You WON")
elif computer_choice > user_choice:
    print("You lost")
elif computer_choice < user_choice:
    print("You WON")
