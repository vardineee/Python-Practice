
import random
from art import logo


EASY_LEVEL_ATTEPTS = 10
HARD_LEVEL_ATTEPTS = 5




def check_answer( user_guess, chosen_number, attempts):
    if user_guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
    elif user_guess < chosen_number:
         print("Too low")
         print("Guesss again")
         return attempts - 1
    elif user_guess > chosen_number:
         print("Too High")
         print("Guesss again")
         return attempts - 1


def difficulty_level():
    difficulty_type = input(f"Choose a difficulty type. Type 'easy' or 'hard': ").lower()
    if difficulty_type == 'easy':
         return EASY_LEVEL_ATTEPTS
    else:
        return  HARD_LEVEL_ATTEPTS


def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    chosen_number = random.randint(1,100)
    print(f"andom chosen number is: {chosen_number}")
    attempts = difficulty_level()


    user_guess = 0
    while user_guess != chosen_number:
        print(f"You have {attempts} attempts remaning to guess a number")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, chosen_number, attempts)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return

game()
