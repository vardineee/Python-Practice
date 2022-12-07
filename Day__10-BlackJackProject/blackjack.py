import random
import os
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(card_list):
    '''Takes a list of cards and calculate the sum '''
    if sum(card_list) == 21  and len(card_list)==2:
        return 0
    if  11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(user_score, computer_score):

    if user_score > 21 and computer_score > 21:
        return "You lose"
    elif computer_score == 0:
        return "Opponent wins BlackJack"
    elif user_score == 0:
        return "You win BlackJack"
    elif computer_score ==user_score:
        return "Draw"
    elif user_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "Opponent went over, you win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose, opponent wins"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for  _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to continue or 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

        while computer_score !=0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, your final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

while input("Do you want to play a game BlackJack? Type 'y' or 'no': ").lower():
    os.system('clear')
    play_game()
