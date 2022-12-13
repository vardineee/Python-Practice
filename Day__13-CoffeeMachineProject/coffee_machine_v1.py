from menu_data import MENU, resources

water = resources['water']
milk = resources["milk"]
coffee = resources["coffee"]
coffee_machine_money = 0

quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01


def report():
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${coffee_machine_money}"


def check_resources(user_choice):

    for drink, value in MENU.items():
        if user_choice == "espresso":
            if coffee >= value["ingredients"]["coffee"]:
                if water >= value["ingredients"]['water']:
                    return True
                else:
                    return "Sorry, there is not enough water"
            else:
                return "Sorry, there is not enough water"

        elif user_choice == drink:
            if coffee >= value["ingredients"]["coffee"]:
                if water >= value["ingredients"]['water']:
                    if milk >= value["ingredients"]["milk"]:
                        return True
                    else:
                        return "Sorry, there is not enough milk"
                else:
                    return "Sorry, there is not enough water"
            else:
                return "Sorry, there is not enough coffee"


def process_coins(quarters, dimes, nickels, pennies):
    monetary_value = (quarters * quarter_value) + (dimes * dime_value) + (
        nickels * nickel_value) + (pennies * penny_value)
    return monetary_value


def check_transaction(user_money, user_input):
    if user_money < coffee_cost:
        return "Sorry that's not enough money. Money refunded."

    elif user_money == coffee_cost:
        print(f"Here is your {user_input}. Enjoy!")
        return True
    elif user_money > coffee_cost:
        change = round(user_money - coffee_cost, 2)
        print(f"Here is {change} dollars in change.")
        print(f"Here is your {user_input}. Enjoy!")
        return True


turn_off = False
while not turn_off:

    user_input = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        turn_off = True
    elif user_input == "report":
         print(report())
    else:
        user_choice = check_resources(user_input)
        coffee_cost = MENU[user_input]["cost"]
        if user_choice == True:
            print("Please insert your coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dims?: "))
            nickels = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            user_money = process_coins(quarters, dimes, nickels, pennies)
            payment = check_transaction(user_money, user_input)
            if payment == True:
                water -= MENU[user_input]["ingredients"]["water"]
                if user_input == "espresso":
                    milk -= 0
                else:
                    milk -= MENU[user_input]["ingredients"]["milk"]
                    coffee -= MENU[user_input]["ingredients"]["coffee"]
                    coffee_machine_money += MENU[user_input]["cost"]
                print(report())
            else:
                print(payment)
                print(report)
        else:
            print(user_choice)
            print(report())
            turn_off = True
