# Start the game by asking the player:
#
# *"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*
#
# From there you will need to figure out:
# * How you will store the user's input.
# * How you will generate a random choice for the computer.
# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
# * And also how you will give feedback to the player.

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [paper, rock, scissors]
user_choice = input("Enter your choice: rock, paper or scissors. ").lower()
if user_choice == "rock":
    print(f"User choice is\n {rock}")
elif user_choice =="paper":
    print(f"User choice is\n {paper}")
else:
    print(f"User choice is\n {scissors}")

computer_choice = random.choice(choices)
print(f"Computer choice is\n {computer_choice}")

if user_choice == "paper" and computer_choice == rock:
    print("User wins!")
elif user_choice == "paper" and computer_choice == scissors:
    print("Computer wins!")
elif user_choice == "scissors" and computer_choice == paper:
    print("User wins!")
elif user_choice == "scissors" and computer_choice == rock:
    print("Computer wins!")
elif user_choice == "rock" and computer_choice == paper:
    print("Computer wins!")
elif user_choice =="rock" and computer_choice ==scissors:
    print("User wins!")
else:
    print("It's a draw. Try again")
