from art import logo,vs
from game_data import data
import random
import os

print(logo)
def format_data(account):
    '''Format data in a printable format '''
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f" {account_name}, a {account_desc}, from {account_country}."

def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        if guess == "a":
            return True
        else:
            return False
    if b_follower_count > a_follower_count:
        if guess == "b":
            return True
        else:
            return False
score = 0
continue_game = True
account_b=random.choice(data)


while continue_game:
    account_a=account_b
    account_b=random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")



    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system("clear")
    
    if is_correct == True:
        score +=1
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")
