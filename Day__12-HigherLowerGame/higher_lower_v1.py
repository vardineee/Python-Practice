from game_data import data
from random import randint
from art import logo,vs

print(logo)


def candidate_1():

    random_choice = randint(0,len(data)-1)
    name = data[random_choice]['name']
    description = data[random_choice]['description']
    country = data[random_choice]['country']
    print(f"Compare A: {name}, a {description}, from {country}.")
    return    data[random_choice]['follower_count']


def candidate_2():
    print(vs)
    random_choice = randint(0,len(data)-1)
    name = data[random_choice]['name']
    description = data[random_choice]['description']
    country = data[random_choice]['country']

    print(f"Compare B: {name}, a {description}, from {country}.")
    return    data[random_choice]['follower_count']



score = 0
try_again = True

while try_again:
    a_candidate = candidate_1()
    b_condidate = candidate_2()
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if user_choice == "A":
        if a_candidate > b_condidate:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    else:
        if b_condidate > a_candidate:
            score +=1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break


    while score == 0:
        try_again = False
