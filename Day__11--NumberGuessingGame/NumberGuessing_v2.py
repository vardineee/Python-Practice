
import random
from art import logo

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_number = random.randint(1,100)
print(f"andom chosen number is: {chosen_number}")
difficulty_type = input(f"Choose a difficulty type. Type 'easy' or 'hard': ").lower()




def easy():
    if difficulty_type == 'easy':
        attempts = 10
    else:
        attempts = 5
    if attempts !=0:
        game_end = False

    while not game_end:
        print(f"You have {attempts} attempts remaning to guess a number")
        if attempts == 0:
            print("You've run out of guesses, you lose")
            game_end = True
            break
        user_guess = int(input("Make a guess: "))
        if user_guess == chosen_number:
            print("You won!")
            game_end =True
        elif user_guess < chosen_number:
              attempts -=1
              print("Too low")
              print("Guesss again")
        elif user_guess > chosen_number:
            attempts -= 1
            print("Too High")
            print("Guesss again")

easy()
