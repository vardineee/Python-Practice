import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")


all_bids = {}
def highest_bid(name, bid):
    all_bids[name] = bid
    highest_bid = 0
    for key,value in all_bids.items():
        if value > highest_bid:
            highest_bid = value
            bidder_name = key
    print(f"The winner is {bidder_name} a bid of {highest_bid}")



should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    try_again = input("Are there any other bidders? Type 'yes' or 'no'?").lower()
    highest_bid(name, bid)
    if try_again == "no":
        should_continue = False
    else:
        os.system("clear")
