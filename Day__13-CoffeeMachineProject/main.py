MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
water = resources['water']
milk = resources["milk"]
coffee = resources["coffee"]
coffee_machine_money = 0

quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01


def report():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {coffee_machine_money}")
    return


def check_resources(user_choice):

    for drink, value in MENU.items():
        if drink == user_choice:
            if coffee >= value["ingredients"]["coffee"]:
                if water >= value["ingredients"]['water']:
                    if milk >= value["ingredients"]["milk"]:
                        return True,  value['cost']
                    else:
                        return "Sorry, there is not enough milk"
                else:
                    return "Sorry, there is not enough water"
            else:
                return "Sorry, there is not enough coffee"


def process_coins(quarters,dimes,nickels,pennies):
    monetary_value = (quarters *quarter_value) + (dimes*dime_value) +(nickels*nickel_value) + (pennies *penny_value)
    return monetary_value

def check_transaction(user_money):
    if user_money < coffee_cost:
        return "Sorry that's not enough money. Money refunded."
    elif user_money == coffee_cost:
        return coffee_machine_money + user_money
    elif user_money > coffee_cost:
        change = round(user_money - coffee_cost, 2)
        return  f"Here is {change} dollars in change."






turn_off = False
while not turn_off:
    coffee_cost = 0
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report()
    print(user_input)
    user_choice = check_resources(user_input)
    print(user_choice)
    if user_choice[0] == True:
        coffee_cost += user_choice[1]
        print("Please insert your coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dims?: "))
        nickels = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        user_money = process_coins(quarters, dimes, nickels, pennies)
        payment = check_transaction(user_money)
        print(payment)


    if user_input == "off":
        turn_off = True


